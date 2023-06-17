# PostMan
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Социальная+Сеть)](https://git.io/typing-svg)



# Установка django

### 1) Создать виртуальное окружение установить зависимости
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

### 2) Выполнить миграции, cоздать суперпользователя и запустить сервер

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
