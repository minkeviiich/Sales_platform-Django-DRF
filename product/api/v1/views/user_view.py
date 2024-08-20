from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import Balance
from django.core.exceptions import ValidationError
from drf_spectacular.utils import extend_schema

from api.v1.serializers.user_serializer import CustomUserSerializer, BalanceSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ["get", "head", "options"]
    permission_classes = (permissions.IsAdminUser,)

class BalanceViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    @action(
        detail=False, 
        methods=['get']
    )
    def user_balance(self, request):
        user = request.user
        balance = user.balance.balance
        return Response({'balance': balance}, status=status.HTTP_200_OK)

    # TODO
    @action(
        detail=True, 
        methods=['get'], 
        permission_classes=[permissions.IsAdminUser]
    )
    def balance(self, request, pk=None):
        try:
            balance = Balance.objects.get(user__id=pk)
            return Response({'balance': balance.balance}, status=status.HTTP_200_OK)
        except Balance.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    # TODO
    @extend_schema(
        request=BalanceSerializer,
        responses={200: BalanceSerializer}
    )
    @action(
        detail=True, 
        methods=['post'], 
        permission_classes=[permissions.IsAdminUser]
    )
    def update_balance(self, request, pk=None):
        try:
            balance = Balance.objects.get(user__id=pk)
            serializer = BalanceSerializer(data=request.data)
            if serializer.is_valid():
                amount = serializer.validated_data['amount']
                if request.user.is_staff:
                    balance.balance += amount
                    balance.save()
                    return Response({'balance': balance.balance}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Balance.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
