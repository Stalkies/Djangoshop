from django.contrib import admin
from web.models import Goods, Category
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ("title", "system_info", "price")
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]