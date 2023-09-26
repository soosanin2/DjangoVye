from rest_framework.serializers import ModelSerializer

from comments.models import Article


class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = ['author', 'title', 'text', 'created_at']

