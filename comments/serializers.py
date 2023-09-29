from rest_framework.fields import ReadOnlyField, DateTimeField
from rest_framework.serializers import ModelSerializer

from comments.models import Article, Commentary


class ArticleSerializer(ModelSerializer):
    author_username = ReadOnlyField(source='author.username')
    created_at = DateTimeField(format="%d.%m.%Y в %H:%M", read_only=True)
    class Meta:
        model = Article
        fields = ['title', 'text', 'created_at', 'author_username', 'id']


class CommentarySerializer(ModelSerializer):


    class Meta:
        model = Commentary
        fields = ['__all__']

