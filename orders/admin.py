from django.contrib import admin
from .models import Order,OrderItems

# Register your models here.

class OrderItemInLine(admin.TabularInline):
    model = OrderItems
    raw_id_fields = ('product',)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','updated','paid')
    list_filter = ('paid',)
    inlines = (OrderItemInLine,)