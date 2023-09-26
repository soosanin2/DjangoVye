from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from comments.views import article_page, ArticleView, article_app

router = SimpleRouter()

router.register('api/comments', ArticleView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', article_page),
    path('art_page/', article_app),

]
urlpatterns += router.urls
