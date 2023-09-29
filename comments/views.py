from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.viewsets import ModelViewSet

from comments.forms import ArticleForm
from comments.models import Article
from comments.serializers import ArticleSerializer
from django.urls import reverse, reverse_lazy


def my_view(request):
    page_title = "Моя HTML страница"  # Здесь вы устанавливаете название страницы
    return render(request, 'my_template.html', {'page_title': page_title})


class HomeListView(ListView):
    model = Article
    template_name = 'main_app.html'
    context_object_name = "list_articles"


class DetailListView(DetailView):
    model = Article
    template_name = 'detail_page.html'
    context_object_name = "get_article"


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'edit_page.html'
    form_class = ArticleForm
    success_url = reverse_lazy("edit_page")

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Article.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'edit_page.html'
    form_class = ArticleForm
    success_url = reverse_lazy("edit_page")

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'edit_page.html'
    success_url = reverse_lazy("edit_page")


# http://127.0.0.1:8008/api/post/?format=json

class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


def article_app(request):
    return render(request, "main_app.html")
