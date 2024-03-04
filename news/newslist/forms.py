from .models import Article
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticleForm(ModelForm):
    class Meta:
        model=Article
        fields=['header', 'text', 'dateTime']

        widgets={
            'header':TextInput(attrs={
                'class':'inputform inputname',
                'placeholder':'Название'
            }),
            'text':Textarea(attrs={
                'class':'inputform',
                'placeholder':'Текст'
            }),
            'dateTime': DateTimeInput(attrs={
                'class': 'inputform inputdate',
                'placeholder': 'Дата и время'
            })
        }