from django.contrib import admin

from .models import Article, UserDownloads, Commentary

admin.site.register(Article)
admin.site.register(UserDownloads)
admin.site.register(Commentary)
