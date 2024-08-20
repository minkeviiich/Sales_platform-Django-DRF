# Выполненное тестовое задание Django/Backend
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
### Связи таблиц
Ознакомиться можно тут: https://drive.google.com/file/d/16eVCytLDfPVJETPjmCf_sZfbmrZRwJ_L/view?usp=sharing

## Установка на локальном компьютере
### 1. Клонируйте репозиторий:
```
git clone git@github.com:minkeviiich/test-backend.git
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


### __Технологии__
* [Python 3.10.12](https://www.python.org/doc/)
* [Django 4.2.10](https://docs.djangoproject.com/en/4.2/)
* [Django REST Framework  3.14.0](https://www.django-rest-framework.org/)
* [Djoser  2.2.0](https://djoser.readthedocs.io/en/latest/getting_started.html)
* [PostgreSQL 14](https://www.postgresql.org/docs/14/index.html)
* [Docker-Compose](https://docs.docker.com/compose/release-notes/)
