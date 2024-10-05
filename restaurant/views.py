from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets
#from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing booking instances.
    """
    queryset = Booking.objects.all()  # Fetches all booking objects
    serializer_class = BookingSerializer  # Uses the BookingSerializer
