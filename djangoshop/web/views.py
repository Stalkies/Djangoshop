from email.policy import HTTP
from http.client import HTTPResponse
from unicodedata import category
from urllib.error import HTTPError
from django.shortcuts import render
from web.models import Goods, Category
# Create your views here.
def index(request):
    goods = Goods.objects.all()
    categories = Category.objects.all()

    context = {
        'goods': goods,
        'categories': categories,
    }
    return render(request, "index.html", context=context)
def category(request, slug):
    categories = Category.objects.all()
    goods = Goods.objects.all()
    for i in categories:
        if i.title == slug.capitalize() or i.title == slug.upper():
            i.state = '__active'
            return render(request, 'index.html', context={'categories': categories, 'slug': slug, 'goods' : goods})

    responce = render(request, '404.html')
    responce.status_code = 404
    return responce
