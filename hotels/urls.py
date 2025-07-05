from django.urls import path
from . import views

app_name = 'hotels'  # Пространство имён для маршрутов

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),  # Главная страница
    path('hotels/', views.hotel_list, name='hotel_list'),  # Альтернативный путь
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]
