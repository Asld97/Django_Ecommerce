from django.contrib import admin
from .models import Product, Category

# Register your models here - short version
# admin.site.register(Product)
# admin.site.register(Category)

# More flexible way
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} # Fill in field before its specific data  - never empty field

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable= ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)} # Fill in field before its specific data - never empty field