from django.contrib import admin
from app1.models import Product,Order
# Register your models here.




class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","name", "catogory"  ,  "quantity"]
    list_filter = ["catogory"]



admin.site.site_header= "OnlineBook"




admin.site.register(Product,ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product',"staff","order_quantity","date"]
    list_filter = ["staff"]



admin.site.register(Order,OrderAdmin)