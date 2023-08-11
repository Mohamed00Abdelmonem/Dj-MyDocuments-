from django.urls import path

from .views import index, section

urlpatterns = [
    
path('index/', index),
path('index/section/python', section, name='index'),

    
]