from django.urls import path

from djax import views

urlpatterns = [
    path('', views.AddressView.as_view(), name='address-view'),
    path('form-data/', views.AddressDataView.as_view(), name='address-data-view'),
]