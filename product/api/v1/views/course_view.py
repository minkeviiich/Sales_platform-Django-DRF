from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.exceptions import ValidationError

from api.v1.permissions import IsStudentOrIsAdmin, ReadOnlyOrIsAdmin, make_payment
from api.v1.serializers.course_serializer import (CourseSerializer,
                                                  CreateCourseSerializer,
                                                  CreateGroupSerializer,
                                                  CreateLessonSerializer,
                                                  GroupSerializer,
                                                  LessonSerializer)
from api.v1.serializers.user_serializer import Subscription
from courses.models import Course, Group
from django.db import transaction


class LessonViewSet(viewsets.ModelViewSet):
    """Уроки."""

    permission_classes = (IsStudentOrIsAdmin,)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LessonSerializer
        return CreateLessonSerializer

    def perform_create(self, serializer):
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        serializer.save(course=course)

    def get_queryset(self):
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        return course.lessons.all()


class GroupViewSet(viewsets.ModelViewSet):
    """Группы."""

    permission_classes = (permissions.IsAdminUser,)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return GroupSerializer
        return CreateGroupSerializer

    def perform_create(self, serializer):
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        serializer.save(course=course)

    def get_queryset(self):
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        return course.groups.all()


class CourseViewSet(viewsets.ModelViewSet):
    """Курсы """

    queryset = Course.objects.all()
    permission_classes = (ReadOnlyOrIsAdmin,)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CourseSerializer
        return CreateCourseSerializer

    @action(methods=['get'], 
        detail=False, 
        permission_classes=(permissions.IsAuthenticated,)
    )

    def available_courses(self, request):
        user = request.user
        # Получаем список курсов, на которые пользователь еще не подписан

        subscribed_courses = Subscription.objects.filter(user=user).values_list('course_id', flat=True)
        available_courses = Course.objects.exclude(id__in=subscribed_courses)
        serializer = self.get_serializer(available_courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(
        methods=['post'],
        detail=True,
        permission_classes=(permissions.IsAuthenticated,)
    )
    
    def pay(self, request, pk):
        """Покупка доступа к курсу (подписка на курс)."""
        course = self.get_object()
        user = request.user
        try:
            make_payment(user, course)
            # Списываем бонусы и создаем подписку только если проверка прошла успешно
            user.balance.balance -= course.price
            user.balance.save()
            Subscription.objects.create(user=user, course=course)

            # Распределение студента в группу
            self.assign_student_to_group(course, user)

            return Response({'status': 'payment successful'}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def assign_student_to_group(self, course, student):
        groups = Group.objects.filter(course=course)
        if not groups.exists():
            raise ValueError("No groups available for this course.")
        
        # Найти группу с наименьшим количеством студентов
        group = min(groups, key=lambda g: g.students.count())
        group.students.add(student)
        group.save()