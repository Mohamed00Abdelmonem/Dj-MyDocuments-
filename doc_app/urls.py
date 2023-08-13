from django.urls import path

from .views import Section_List, Subject_list, Subject_Detail, Dashboard, Dashboard_detail

urlpatterns = [
    
path('', Section_List.as_view(), name='home'),
path('section/<int:id>', Subject_list,name= 'section_detail'),
path('section/<int:id>/<int:pk>', Subject_Detail.as_view(), name= 'subject_detail'),
path('dashboard/',Dashboard , name='dashboard'),
path('dashboard/<int:id>',Dashboard_detail , name='dashboard_detail'),

]

