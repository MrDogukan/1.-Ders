from django.urls import path
from fscohort.views import index

urlpatterns = [
    path('home/', index),
    
]
