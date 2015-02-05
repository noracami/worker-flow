from django.db import models

# Create your models here.

class worker(models.Model):
    """docstring for worker"""
    class Meta:
        verbose_name = "人員"
    name = models.CharField("姓名", max_length=10)
    location = models.CharField("單位", max_length=60)
    title = models.CharField("職稱", max_length=20)



