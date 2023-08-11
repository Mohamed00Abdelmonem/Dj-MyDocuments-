from django.shortcuts import render
from .models import detail_subject, Subject, Section
from django.views.generic import ListView, DeleteView

# Create your views here.
class Section_List(ListView):
    model = Section
    template_name = 'index.html'


# def index(request):
#     return render(request, 'index.html')

class Section_Detail(DeleteView):
    model = Section
    template_name = 'python-programming.html'


# def section(request):
#     return render(request, 'python-programming.html')