from django.contrib import admin
from product.models import Weight, Product

@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display = ("weight_range", "price", )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", )
    list_filter = ("status", )
