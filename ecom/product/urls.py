from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('products',views.products,name="products"),
    path('view_products/',views.list_products),
    path('add_products/',views.add_products),
    path('edit_products/',views.edit_products),
    path('delete_products/',views.delete_products),

]
