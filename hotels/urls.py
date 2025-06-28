from django.urls import path
from . import views

app_name = 'hotels'

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]