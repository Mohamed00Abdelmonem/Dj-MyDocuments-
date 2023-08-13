from django.shortcuts import render
from .models import Subject, Section
from django.views.generic import ListView, DetailView

# Create your views here.
class Section_List(ListView):
    model = Section
    template_name = 'index.html'



def Subject_list(request, id):
    data = Section.objects.get(id=id)
    subject = Subject.objects.filter(section=data)
    return render(request, 'topic_main.html', {'subject_list':subject, 'data':data})



class Subject_Detail(DetailView):
    model = Subject
    template_name = 'topic_detail.html'


def Dashboard(request):
    data = Subject.objects.all()
    return render(request, 'dashboard.html', {'data':data})    