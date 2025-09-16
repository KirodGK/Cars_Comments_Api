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

# Документация API

Автодокументация API доступна по пути:  
[http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

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

# Автор

**Телеграм**: [@KirodGK_2_0](https://t.me/KirodGK_2_0)  
**Email**: [KirodGK@gmail.com](mailto:KirodGK@gmail.com)
