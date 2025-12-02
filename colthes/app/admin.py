from django.contrib import admin
from .models import clothes,order,CustomerReview,Message
# Register your models here.

@admin.register(clothes)
class clothes(admin.ModelAdmin):
    list_display=['image','cloth_name','fashion_name','price']

@admin.register(order)
class order1(admin.ModelAdmin):
    list_display=['quantity','cloth_name','size','email','phone','address']

@admin.register(CustomerReview)
class Customer_rating(admin.ModelAdmin):
    list_display=['info']

@admin.register(Message)
class message(admin.ModelAdmin):
    list_display=['name','email','subject','message']
