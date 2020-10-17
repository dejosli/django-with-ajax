from django.urls import path

from djax import views

urlpatterns = [
    path('', views.AddressView.as_view(), name='address-view'),
    path('create/', views.address_create_view, name='create-view'),
    path('retrieve/', views.address_retrieve_view, name='retrieve_view'),
]