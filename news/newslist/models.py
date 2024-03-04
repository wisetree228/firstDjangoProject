from django.db import models


class Article(models.Model):
    header=models.CharField('Название', max_length=50)
    text=models.TextField('Текст', max_length=10000)
    dateTime=models.DateTimeField('Время и дата')
    def __str__(self):
        return self.header
    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'
    def get_absolute_url(self):
        return f'/{self.id}'
# Create your models here.

#commi 1
