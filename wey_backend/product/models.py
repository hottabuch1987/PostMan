from django.db import models

from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=255, verbose_name='имя')
    slug = models.SlugField(verbose_name='слаг')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='цена')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name='фото')
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name='миниатюра')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')
    quantity = models.PositiveIntegerField("Количество", default=0)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('-date_added',)

    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail