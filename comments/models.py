from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


def download_user_img(instance, filename):
    user_id_name = str(instance.user.id)+str(instance.user.username)
    return f'uploads/img/{user_id_name}/{filename}'


def download_user_text(instance, filename):
    user_id_name = str(instance.user.id)+str(instance.user.username)
    return f'uploads/text/{user_id_name}/{filename}'


def download_user_avatar(instance, filename):
    user_id_name = str(instance.user.id)+str(instance.user.username)
    return f'uploads/avatar/{user_id_name}/{filename}'


class UserDownloads(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    download_avatar = models.FileField(upload_to=download_user_avatar, blank=True, null=True, verbose_name="Your avatar")
    download_img = models.FileField(upload_to=download_user_img, blank=True, null=True, verbose_name="Your image")
    download_text = models.FileField(upload_to=download_user_text, blank=True, null=True, verbose_name="Your text file")
    home_page = models.URLField(max_length=255, blank=True, null=True, verbose_name="Home Page", )

    def __str__(self):
        return self.username

    def get_avatar_url(self):
        if self.download_avatar:
            return self.download_avatar.url
        return 'media/avatars/No_image.png'


class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Commentary(models.Model):
    binding = models.IntegerField(verbose_name="Binding", blank=True, null=True)
    binding_com = models.IntegerField(verbose_name="Binding_com", blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    captcha = models.CharField(max_length=255, verbose_name="Captcha")
    text = models.TextField(verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentarys"



