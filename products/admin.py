from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
  list_display = ("title",)
#   prepopulated_fields = {"slug": ("title", "uuid")}

  
admin.site.register(Product, ProductAdmin)
