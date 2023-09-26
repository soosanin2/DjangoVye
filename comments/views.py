from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from comments.models import Article
from comments.serializers import ArticleSerializer


def article_page(request):
    return render(request, "index.html", {"articles": Article.objects.all()})
# http://127.0.0.1:8000/api/comments/?format=json

class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

