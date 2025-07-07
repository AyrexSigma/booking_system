from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    stars = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    has_pool = models.BooleanField(default=False)
    has_spa = models.BooleanField(default=False)
    has_conference_rooms = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({'★' * self.stars}{'☆' * (5 - self.stars)}"

class Room(models.Model):
    ROOM_TYPES = (
        ('STD', 'Standard'),
        ('DLX', 'Deluxe'),
        ('SUITE', 'Suite'),
        ('FMLY', 'Family')
    )

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.CharField(max_length=5, choices=ROOM_TYPES)
    room_number = models.CharField(max_length=10)
    capacity = models.PositiveSmallIntegerField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=False)
    feature = models.TextField(blank=True)

    def __str__(self):
        return  f"{self.get_room_type_display()} #{self.room_number} at {self.hotel.name}"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Очікує підтвердження'),
        ('confirmed', 'Підтверджено'),
        ('cancelled', 'Скасовано'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Бронювання #{self.id}"

    def can_be_cancelled(self):
        return self.status == 'pending' and self.check_in > timezone.now().date()

    @admin.display(boolean=True, description='Підтверджено?')
    def is_confirmed(self):
        return self.status == 'confirmed'