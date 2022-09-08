from django.db import models
from djangoshop.settings import LANGUAGE_CODE

class Category(models.Model):
    title = models.CharField(max_length=32, verbose_name='Name')
    slug = models.CharField(max_length=32, verbose_name='slug', blank=True)
    def __str__(self):
        return self.title
    class Meta:
        if LANGUAGE_CODE == 'ru-ru':
            verbose_name_plural = 'Категории'
            verbose_name = 'Категорию'
        else:
            verbose_name_plural = 'Categories'
            verbose_name = 'Category'
    
    

class Goods(models.Model):
    title = models.CharField(max_length=32,verbose_name='Название')
    INFORMATION = (
        ('macOS', 'macOS'),
        ('Windows', 'Windows'),
        ('iOS', 'iOS'),
        ('Android', 'Android'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    system_info = models.CharField(max_length=20, choices=INFORMATION, blank=True, verbose_name='Операционная система')
    price = models.FloatField(max_length=20, verbose_name='Цена')
    picture = models.ImageField(upload_to='laptops/', default='noimage.png')
    manufacturer = models.CharField(max_length=32, blank=True)
    class Meta:
        if LANGUAGE_CODE == 'ru-ru':
            verbose_name_plural = 'Товары'
            verbose_name = 'Товар'
        else:
            verbose_name_plural = 'Goods'
            verbose_name = 'Good'
    def get_price(self):
        if self.price == int(self.price):
            self.price = int(self.price)
        return self.price
    def __str__(self):
        return self.title