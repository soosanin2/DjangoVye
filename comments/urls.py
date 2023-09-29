from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views
from .views import article_app, ArticleView

router = SimpleRouter()

router.register('api/post', ArticleView)

# http://127.0.0.1:8008/api/post/?format=json


urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('', views.article_app, name='article_app'),
    path('detail/<int:pk>', views.DetailListView.as_view(), name='detail_page'),
    path('edit-page', views.ArticleCreateView.as_view(), name='edit_page'),
    path('update-page/<int:pk>', views.ArticleUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>', views.ArticleDeleteView.as_view(), name='delete_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('login', views.ProjectLoginView.as_view(), name='login_page'),
    path('logout', views.ProjectLogoutView.as_view(), name='logout_page'),

]

urlpatterns += router.urls
