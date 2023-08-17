from django.urls import path

from .views import (Section_List, Subject_list, Subject_Detail, 
Dashboard, Dashboard_detail, Create_Section,Create_Section, 
Create_Subject, Update_Subject,Update_Section, Delete_Section,Delete_Subject)

urlpatterns = [
    
path('', Section_List.as_view(), name='home'),
path('section/<int:id>', Subject_list,name= 'section_detail'),
path('section/<int:id>/<int:pk>', Subject_Detail.as_view(), name= 'subject_detail'),
path('dashboard/',Dashboard , name='dashboard'),
path('dashboard/<int:id>',Dashboard_detail , name='dashboard_detail'),
path('create_section', Create_Section.as_view(), name='create_section'),
path('create_subject/<int:id>', Create_Subject, name='create_subject'),
path('dashboard/update_subject/<int:pk>', Update_Subject.as_view(), name='update_subject'),
path('dashboard/update_section/<int:pk>', Update_Section.as_view(), name='update_section'),
path('dashboard/delete_section/<int:pk>', Delete_Section.as_view(), name='delete_section'),
path('dashboard/delete_subject/<int:pk>', Delete_Subject.as_view(), name='delete_subject'),

]

