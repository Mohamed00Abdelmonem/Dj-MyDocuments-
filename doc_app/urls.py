from django.urls import path

from .views import Section_List, Section_Detail

urlpatterns = [
    
path('', Section_List.as_view(), name='home'),
path('section/<int:pk>', Section_Detail.as_view(), name= 'section_detail'),

    
]