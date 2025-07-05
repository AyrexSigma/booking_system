from django.urls import path
from . import views

app_name = 'hotels'

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('<int:pk>/', views.hotel_detail, name='hotel_detail'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('bookings/<int:pk>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('bookings/<int:pk>/', views.booking_detail, name='booking_detail'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]