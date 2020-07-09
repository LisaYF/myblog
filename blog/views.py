from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models

def index(request):
    # return HttpResponse('Just Test')
    # article = models.Article.objects.get(pk=1)
    articles = models.Article.objects.all()
    # return render(request,'blog/index.html',{'test':'dict test'})
    return render(request,'blog/index.html',{'articles':articles})

def article_page(request,article_id):
    article=models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})