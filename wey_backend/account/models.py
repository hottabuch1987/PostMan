import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from product.models import Product
from django.utils import timezone



class CustomUserManager(UserManager):
    def _create_user(self, email, name, password, **extra_fields):# name,
        if not email:
            raise ValueError("Вы не указали действительный адрес электронной почты")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)#name=name,
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, email, password, **extra_fields)
    
    def create_superuser(self,  email=None, password=None, **extra_fields):#name=None,
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user( email, password, **extra_fields)#name,

#модель пользователя
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField("Email", unique=True)
    name = models.CharField("Имя", max_length=255, blank=True, default='')
    avatar = models.ImageField("Фото", upload_to='avatars', blank=True, null=True)
    friends = models.ManyToManyField('self')
    friends_count = models.IntegerField(default=0)
    people_you_may_know = models.ManyToManyField('self')
    my_product = models.ForeignKey(Product, related_name='my_product', on_delete=models.CASCADE)
    posts_count = models.IntegerField(default=0)
    is_active = models.BooleanField("Активный", default=True)
    is_superuser = models.BooleanField("Суперпользователь", default=False)
    is_staff = models.BooleanField("Администратор", default=False)
    date_joined = models.DateTimeField("Дата регистрации", default=timezone.now)
    last_login = models.DateTimeField("Последний визит", blank=True, null=True)



    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_avatar(self):
        if self.avatar:
            return 'http://127.0.0.1:8000' + self.avatar.url
        else:
            return 'https://loremflickr.com/320/240'
        
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email} - {self.name}'
    


class FriendshipRequest(models.Model):
    SENT = 'sent'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    STATUS_CHOICES = (
        (SENT, 'Sent'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_for = models.ForeignKey(User, related_name='received_friendshiprequests', on_delete=models.CASCADE)
    created_at = models.DateTimeField("Дата", auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_friendshiprequests', on_delete=models.CASCADE)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default=SENT)

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return f'{self.created_for} - {self.created_by} статус: {self.status}'
