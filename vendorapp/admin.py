from django.contrib import admin
from .models import *


admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(Product, ProductAdmin)
