from django.urls import path
from . import views

urlpatterns = [
    path('stocklist/', views.stock_list, name='stock_list'),
    path('stockinsert/', views.stock_form, name='stock_insert'),
    path('<int:id>/', views.stock_form, name='stock_update'),
    path('delete/<int:id>/', views.stock_delete, name='stock_delete'),
    path('walletlist/', views.wallet_list, name='wallet_list'),
    path('walletinsert/', views.wallet_form, name='wallet_insert'),
    path('<int:id>/', views.wallet_form, name='wallet_update'),
    path('delete/<int:id>/', views.wallet_delete, name='wallet_delete'),
]
