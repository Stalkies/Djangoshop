from django.contrib import admin
from web.models import Goods
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ("title", "system_info", "price")
