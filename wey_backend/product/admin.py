from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',  'price']
    list_filter = [ 'name', 'date_added','slug']
    list_editable = ['price']
    prepopulated_fields = {'slug':('name',)}
    date_hierarchy ='date_added'
  