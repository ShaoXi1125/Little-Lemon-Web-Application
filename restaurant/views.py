from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer
from rest_framework import viewsets
from .models import Booking  # Import your Booking model
from .serializers import BookingSerializer  # Import the BookingSerializer

# Regular Django view (for rendering an HTML page)
def index(request):
    return render(request, 'index.html', {})

# API view to list and create Menu items (GET and POST)
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# API view to retrieve, update, or delete a single Menu item (GET, PUT, DELETE)
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Fetch all booking objects
    serializer_class = BookingSerializer  # Use the BookingSerializer for this view