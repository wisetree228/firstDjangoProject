from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView

# Create your views here.

class NewsDetail(DetailView):
    model=Article
    template_name='newslist/detail.html'
    context_object_name = 'Article'

class NewsUptade(UpdateView):
    model=Article
    template_name = 'newslist/update.html'
    form_class = ArticleForm


def index(request):
    news=Article.objects.order_by('dateTime')
    return render(request, 'newslist/index.html', {'news':news})



def add(request):
    error=''
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('main_page')
        else:
            error='Некорректные данные!'

    form=ArticleForm()
    data={'form':form, 'error':error}
    return render(request, 'newslist/add.html', data)
