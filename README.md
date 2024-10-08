## Online platform for selling courses
### Описание проекта
Этот проект представляет собой онлайн-платформу для продажи образовательных курсов. Платформа позволяет пользователям создавать, публиковать и продавать свои курсы, а также управлять ими. 
Основные функции включают:
- Создание курсов.
- Управление курсами: Возможность редактирования, обновления и удаления курсов.
- Покупка курсов.
- Аналитика и отчеты: Инструменты для отслеживания успеваемости студентов и анализа продаж.
- Подписка на курсы: Студенты могут подписываться на курсы, после чего им открывается доступ к урокам.
- Распределение студентов по группам.

### __Технологии__
* [Python 3.10.12](https://www.python.org/doc/)
* [Django 4.2.10](https://docs.djangoproject.com/en/4.2/)
* [Django REST Framework  3.14.0](https://www.django-rest-framework.org/)
* [Djoser  2.2.0](https://djoser.readthedocs.io/en/latest/getting_started.html)
* [PostgreSQL 14](https://www.postgresql.org/docs/14/index.html)
* [Docker-Compose](https://docs.docker.com/compose/release-notes/)

### Связи таблиц
Ознакомиться можно тут: https://drive.google.com/file/d/16eVCytLDfPVJETPjmCf_sZfbmrZRwJ_L/view?usp=sharing

## Установка на локальном компьютере
### 1. Клонируйте репозиторий:
```
git clone git@github.com:minkeviiich/Sales_platform-Django-DRF.git
```
### 2. Сборка Docker-образа: 
- Убедитесь, что Docker и Docker Compose установлены на вашем компьютере. Вы можете проверить это, выполнив команды:

```
docker --version
docker compose --version
```

- Соберите Docker-образ

```
docker compose build
```

### 3. Запуск Docker Compose:

```
docker compose up
```

- Эта команда создаст и запустит все контейнеры, определенные в файле docker-compose.yml.
- Если вы хотите запустить контейнеры в фоновом режиме, добавьте флаг -d:

```
docker-compose up -d
```

### 4. Создание суперпользователя (если требуется)
- Подключитесь к запущенному контейнеру:

```
docker exec -it <имя_или_ID_контейнера> bash
```

- Например, если имя вашего контейнера app, команда будет:

```
docker exec -it app bash
```

- Чтобы посмотреть имя контейнера в Docker, выполните следующие шаги:
- Откройте терминал.
- Выполните команду для отображения всех запущенных контейнеров:

```
docker ps
```

- Эта команда покажет список всех запущенных контейнеров с их именами, ID, образами и статусом.
- Если вы хотите увидеть все контейнеры, включая остановленные, используйте флаг -a:

```
docker ps -a
```

### __OpenAPI документация__
* Swagger: http://127.0.0.1:8000/api/v1/swagger/
* ReDoc: http://127.0.0.1:8000/api/v1/redoc/

