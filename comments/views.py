from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.viewsets import ModelViewSet

from comments.forms import ArticleForm, AuthUserForm, RegisterUserForm
from comments.models import Article
from comments.serializers import ArticleSerializer
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User


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


class ArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login_page")
    model = Article
    template_name = 'edit_page.html'
    form_class = ArticleForm
    success_url = reverse_lazy("edit_page")

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Article.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login_page")
    model = Article
    template_name = 'edit_page.html'
    form_class = ArticleForm
    success_url = reverse_lazy("edit_page")

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login_page")
    model = Article
    template_name = 'edit_page.html'
    success_url = reverse_lazy("edit_page")


class RegisterUserView(CreateView):
    model = User
    template_name = 'register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class ProjectLoginView(LoginView):
    template_name = 'login_page.html'
    form_class = AuthUserForm
    success_url = reverse_lazy("home")
    def get_success_url(self):
        return self.success_url


class ProjectLogoutView(LogoutView):
    next_page = reverse_lazy("home")






# http://127.0.0.1:8008/api/post/?format=json

class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


def article_app(request):
    return render(request, "main_app.html")
