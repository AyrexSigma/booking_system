from django.contrib import admin
from .models import Hotel, Room, Booking

# Register your models here.
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'stars', 'has_pool')
    list_filter = ('stars', 'has_pool', 'has_spa')
    search_fields = ('name', 'address')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'room_type', 'room_number', 'price_per_night', 'is_available')
    list_filter = ('room_type', 'is_available')
    search_fields = ('room_number', 'hotel__name')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'room', 'check_in', 'check_out', 'status', 'is_confirmed_display')
    list_filter = ('status', 'check_in', 'check_out')
    search_fields = ('user__username', 'room__room_number')
    date_hierarchy = 'check_in'

    @admin.display(boolean=True, description='Підтверджено?')
    def is_confirmed_display(self, obj):
        return obj.status == 'confirmed'