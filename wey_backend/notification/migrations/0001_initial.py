# Generated by Django 3.2.12 on 2023-06-16 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('body', models.TextField(verbose_name='Текст')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('type_of_notification', models.CharField(choices=[('new_friendrequest', 'New friendrequest'), ('accepted_friendrequest', 'Accepted friendrequest'), ('rejected_friendrequest', 'Rejected friendrequest'), ('post_like', 'Post like'), ('post_comment', 'Post comment')], max_length=50, verbose_name='Тип уведомления')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_notifications', to=settings.AUTH_USER_MODEL)),
                ('created_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_notifications', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
            options={
                'verbose_name': 'Оповещение',
                'verbose_name_plural': 'Оповещения',
            },
        ),
    ]
