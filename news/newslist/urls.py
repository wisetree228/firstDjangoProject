from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('/add', views.add, name='add'),
    path('<int:pk>', views.NewsDetail.as_view(), name='news-detail'),
    path('<int:pk>/uptade', views.NewsUptade.as_view(), name='news-uptade')
]