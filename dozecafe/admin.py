from django.contrib import admin
from .models import Coffee, Order, Contact, Blog
# Register your models here.

# TO Modify Product Detalis view for admin
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    list_editable = ['price']
admin.site.register(Coffee, CoffeeAdmin)

# TO Modify Product Detalis view for admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name','product','total_cost']
admin.site.register(Order, OrderAdmin)

admin.site.register(Contact)
admin.site.register(Blog)
