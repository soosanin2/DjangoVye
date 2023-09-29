from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # переопределяем форму(наводим красоту)
    def __int__(self, *args, **kwargs):
        super(ArticleForm, self).__int__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

