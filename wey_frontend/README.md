1)  #запускаем докер
    #docker run -p 127.0.0.1:16379:6379 --name redis-celery -d redis
2)
    #celery -A wey_backend  worker -l info




###python scripts/generate_trends.py
###python scripts/generate_friends_suggestions.py