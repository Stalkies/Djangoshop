from django.shortcuts import render
from web.models import Goods
# Create your views here.
def index(request):
    goods = Goods.objects.all()

    context = {
        'goods': goods
    }
    return render(request, "index.html", context=context)