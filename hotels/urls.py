from django.urls import path
from . import views

app_name = 'hotels'  # Додайте це для простору імен

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),  # Це головна сторінка
    path('hotels/', views.hotel_list, name='hotel_list'),  # Це альтернативний шлях
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]