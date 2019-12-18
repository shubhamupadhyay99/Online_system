
from django.urls import path
from django.contrib import admin
from .views import HomeView, charge, CreateProducts, CustomerProdcutList, UsersProductsList, CreateProducts, UpdateCrudUser, Delete, PurchaseProductsView


urlpatterns = [
path('', HomeView.as_view()),
path('<int:order_pk>/charge', charge, name='charge'),
path('create/', CreateProducts.as_view()),
path('customerlist/', CustomerProdcutList.as_view()),
path('userlist/', UsersProductsList.as_view(), name='detail'),
path('create/', CreateProducts.as_view(), name='createProducts'),
path('userlist/update/<int:pk>/', UpdateCrudUser.as_view(), name='crud_ajax_update'),
path('delete/', Delete.as_view(), name='crud_ajax_delete'),
path('PurchasedProducts/', PurchaseProductsView.as_view()),
]
