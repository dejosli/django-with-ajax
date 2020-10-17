from django.urls import path

from djax import views

urlpatterns = [
    path('', views.AddressView.as_view(), name='address-view'),
    path('create/', views.address_create_view, name='address-create-view'),
]