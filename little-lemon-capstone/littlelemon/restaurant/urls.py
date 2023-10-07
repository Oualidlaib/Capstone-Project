from django.urls import path
from .views import bookingview, menuview, index


urlpatterns = [
  path('', index, name='index'),
  path('booking/', bookingview.as_view()),
  path('menu/', menuview.as_view()),
  
]