from . import views
from django.urls import path

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payment, name='payments'),
    path('order_complete/', views.order_complete, name='order_complete'),
]
