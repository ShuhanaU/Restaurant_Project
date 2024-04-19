from django.contrib import admin
from .models import*

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title',)
    fields=('title',)
admin.site.register(Category,CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display=('title','sub_title','description','category','img')
    fields=('title','sub_title','description','category','img')
admin.site.register(Post,PostAdmin)
# Register your models here.

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=('title',)
    fields=('title',)
admin.site.register(ProductCategory,ProductCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('productname','prdctprc','desc','desc2','img','category')
    fields=('productname','prdctprc','desc','desc2','img','category')
admin.site.register(Product,ProductAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','phonenumber','place','image')
    fields=('user','phonenumber','place','image')
admin.site.register(Profile,ProfileAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('name','email','message')
    fields=('name','email','message')
admin.site.register(Feedback,FeedbackAdmin)

class BookaTableAdmin(admin.ModelAdmin):
    list_display=('username','email','phonenumber','noOfperson','date')
    fields=('username','email','phonenumber','noOfperson','date')
admin.site.register(BookaTable,BookaTableAdmin)

class ShippingAdmin(admin.ModelAdmin):
    list_display=('full_name','address','phone','city','pin_code')
    fields=('full_name','address','phone','city','pin_code')
admin.site.register(Shipping,ShippingAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display=('order','product','quantity')
    fields=('order','product','quantity')
admin.site.register(CartItem,CartItemAdmin)

class UserOrderAdmin(admin.ModelAdmin):
    list_display=('user','subtotal','shipping_details')
    fields=('user','subtotal','shipping_details')
admin.site.register(UserOrder,UserOrderAdmin)