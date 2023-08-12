from django.shortcuts import render
from .models import detail_subject, Subject, Section
from django.views.generic import ListView, DeleteView

# Create your views here.
class Section_List(ListView):
    model = Section
    template_name = 'index.html'


class Section_Detail(DeleteView):
    model = Section
    template_name = 'python-programming.html'
    context_object_name = 'object'

# class Subject_List(ListView):
#     model = Subject
#     template_name = 'python-programming.html'
#     context_object_name = 'subject_list'

def Subject_list(request, id):
    data = Section.objects.get(id=id)
    subject = Subject.objects.filter(section=data)
    return render(request, 'python-programming.html', {'subject_list':subject})