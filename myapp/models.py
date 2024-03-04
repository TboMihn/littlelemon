from django.db import models
from unicodedata import name

# Create your models here.
# Menu Category
# Menu

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)
    
class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)
    
    
class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField()