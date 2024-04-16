from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Guest
from .serializers import GuestSerializer

# Create your views here.

class ListCreateGuestView(ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def perform_create(self, serializer):
        serializer.save()
    

class RetrieveUpdateDestroyGuestView(RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


