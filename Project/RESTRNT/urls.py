
from django.contrib import admin
from  .import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('userLogin',views.userLogin,name="userLogin"),
    path('about',views.about,name="about"),
    path('menu',views.menu,name="menu"),
    path('book',views.book,name="book"),
    path('profile',views.Userprofile,name="profile"),
    path('register',views.register,name="register"),
    path('logout',views.Logout,name="logout"),
    path('contact',views.contact,name="contact"),
    path('update',views.update,name="update"),
    path('add_to_cart',views.add_to_cart,name="add_to_cart"),
    path('get_cart_count',views.get_cart_count,name="get_cart_count"),
    path('edit_cart_item',views.edit_cart_item,name="edit_cart_item"),
    path('remove_from_cart',views.remove_from_cart,name="remove_from_cart"),
    path('cart',views.view_cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    path('singleproduct<int:item_id>',views.singleproduct,name="singleproduct"),
    path('addproduct',views.addproduct,name="addproduct")
    # path('cart',views.cart,name="cart"),
]
