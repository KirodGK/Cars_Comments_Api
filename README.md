**DRF Задача #1: Отзывы об автомобилях**

# Цель проекта:

    Развернуть Django проект, развернуть базу данных, настроить Django Rest Framework.

# Используемый Стек

    1. Python 3.12
    2. Django 5
    3. DRF
    4. Djoser
    5. Pandas
    6. PostgreSQL
    7. drf-spectacular - для автодокументации Swager
    8. postman

# Запуск проекта

1. Создать файл .env в корне проекта из файла .env.example

2. Выполнить команду

```bash
docker compose up --build -d

```

3. Сделать root пользователя для тестов Postman с именем root и паролем 2266 или заменить данные в файле car_api.postman_collection.json на свои

```bash
docker compose web exec bash

```

```bash
python car_comments/manage.py createsuperuser
```
