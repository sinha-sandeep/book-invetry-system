
from app1 import views
from django.urls import path
urlpatterns = [

    path('', views.index ,name="index_page"),
  #  path('staff/', views.staff ,name="staff_page"),
    path('product/', views.product ,name="product_page"),
    path('order/', views.order, name="order_page"),
    path('addproduct/', views.addproduct, name="addproduct_page"),
    path('updateproduct/<int:id>/', views.updateproduct, name="updateproduct_page"),
    path('deleteproduct/<int:id>/', views.deleteproduct, name="deleteproduct_page"),
    path('take_order/', views.takeorder, name="takeorder_page"),
]