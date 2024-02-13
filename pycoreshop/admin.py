from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Order, OrderItem, ShippingAddress


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent']
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total', 'created_at', 'updated_at', 'paid', 'shipped']
    list_filter = ['paid', 'shipped', 'created_at', 'updated_at']
    list_editable = ['paid', 'shipped']

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'address', 'city', 'postal_code', 'country')
    search_fields = ('user__username', 'address', 'city', 'postal_code', 'country')
    list_filter = ('country', 'city')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
