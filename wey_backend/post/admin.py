from django.contrib import admin

from .models import Post, PostAttachment, Trend, Like, Comment


admin.site.register(Post)
admin.site.register(PostAttachment)
admin.site.register(Trend)
admin.site.register(Like)
admin.site.register(Comment)
