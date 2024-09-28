from django.urls import path
from .views import *

urlpatterns = [
    path('addDetail/', GoogleSheetView.as_view(), name='addDetail'),
]