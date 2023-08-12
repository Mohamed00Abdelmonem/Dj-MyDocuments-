from django.urls import path

from .views import Section_List, Subject_list, Subject_Detail

urlpatterns = [
    
path('', Section_List.as_view(), name='home'),
# path('section/<int:pk>', Section_Detail.as_view(), name= 'section_detail'),
path('section/<int:id>', Subject_list,name= 'section_detail'),
path('section/<int:id>/<int:pk>', Subject_Detail.as_view(), name= 'subject_detail'),

]

