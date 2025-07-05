from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Hotel, Room, Booking
from .forms import BookingForm

def hotel_list(request):
    """View for hotels list"""
    hotels = Hotel.objects.all().order_by('stars')
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})

def room_detail(request, room_id):
    """View for the room details with the booking form"""
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.user = request.user
            booking.save()
            messages.success(request, 'The booking has been successfully created!')
            return redirect('hotels:my_bookings')  # Исправлено с namespace
    else:
        form = BookingForm()

    return render(request, 'hotels/room_detail.html', {
        'room': room,
        'form': form
    })

@login_required
def my_bookings(request):
    """Сторінка з бронюваннями поточного користувача"""
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'hotels/my_bookings.html', {'bookings': bookings})
