import uuid

from django.db import models
from django.utils.timesince import timesince

from account.models import User

#like
class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return f'{self.id}:{self.created_by} {self.created_at}'

#Comment
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
    
    def created_at_formatted(self):
       return timesince(self.created_at)
    
    def __str__(self):
        return f'{self.id}:{self.body} {self.created_at} {self.created_by}'


#Добавление фото в пост
class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField("Фото", upload_to='post_attachments')
    created_by = models.ForeignKey(User, related_name='post_attachments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.image} - {self.created_by}'
    
    class Meta:
        verbose_name = 'Фото Поста'
        verbose_name_plural = 'Фото Постов'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        else:
            return 'https://loremflickr.com/320/240'

#пост
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField("Текст", blank=True, null=True)

    attachments = models.ManyToManyField(PostAttachment, blank=True)
    is_private = models.BooleanField("Приватное", default=False)
    reported_by_users = models.ManyToManyField(User, blank=True)
    
    likes = models.ManyToManyField(Like, blank=True)
    likes_count = models.IntegerField(default=0)

    comments = models.ManyToManyField(Comment, blank=True)
    comments_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def created_at_formatted(self):
       return timesince(self.created_at)
    
    def __str__(self):
        return f'Пост - {self.body}. Лайков - {self.likes_count}. Коментариев {self.comments_count}'
    
#Популярное
class Trend(models.Model):
    hashtag = models.CharField(max_length=255)
    occurences = models.IntegerField()

    class Meta:
        verbose_name = 'Популярное'
        verbose_name_plural = 'Популярные'

    def __str__(self):
        return f'{self.hashtag} - {self.occurences}'