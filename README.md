### Почтальон - Социальная сеть

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
