### [![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Социальная+сеть+Почтальон)](https://git.io/typing-svg)

# Установка django
### 1) Создать виртуальное окружение и установить зависимости
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

### 2) Выполнить миграции, создать суперпользователя и запуск сервера
    python manage.py makemigrations
    python manage.py migrate    
    python manage.py createsuperuser
    python manage.py runserver
    
# Установка и запуск сервера vue
    npm i
    npm run dev
#
# cкрипты запуска трендов и возможных друзей
    python scripts/generate_trends.py
    python scripts/generate_friends_suggestions.py


[Страница профиля](https://raw.github.com/hottabuch1987/Postman/main/preview/profile.png)
###
[Страница регистрации](https://raw.github.com/hottabuch1987/Postman/main/preview/register.png)
