from celery import shared_task

@shared_task
def minus():
    return 10-2