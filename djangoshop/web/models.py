from distutils.command.upload import upload
from email.policy import default
from django.db import models

class Goods(models.Model):
    title = models.CharField(max_length=20,verbose_name='Название')
    SYSTEM_CHOICES = (
        ('MACOS', 'macOS'),
        ('WINDOWS', 'Windows')
    )
    system_info = models.CharField(max_length=20, choices=SYSTEM_CHOICES, default='WINDOWS', verbose_name='Операционная система')
    price = models.FloatField(max_length=20, verbose_name='Цена')
    picture = models.ImageField(upload_to='laptops/', default='noimage.png')
    class Meta:
        verbose_name_plural = 'Товары'
