from django.urls import path

from .views import *

app_name = 'guest'

urlpatterns = [
    path('', ListCreateGuestView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyGuestView.as_view()),
]