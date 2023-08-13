from django.shortcuts import render
from .models import Subject, Section
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
    data = Section.objects.all()
    return render(request, 'dashboard.html', {'data':data})    

def Dashboard_detail(request, id):
    data = Section.objects.get(id=id)
    topics = Subject.objects.filter(section=data)
    return render(request, 'dashboard_detail.html', {'data':data, 'topics':topics})    


class Create_Section(CreateView):
    model = Section
    template_name = 'create_section.html'
    fields = '__all__'
    success_url = 'dashboard'


class Create_Subject(CreateView):
    model = Subject
    template_name = 'create_subject.html'
    fields = '__all__'
    success_url = 'dashboard'    


class Update_Section(UpdateView):
    model = Section
    fields = '__all__'    
    template_name = 'update_form.html'
    success_url = 'dashboard'    


class Update_Subject(UpdateView):
    model = Subject
    fields = '__all__'    
    template_name = 'update_form.html'
    success_url = 'dashboard'    


class Delete_Section(DeleteView):
    model = Section
    success_url = 'dashboard'    
    template_name = 'delete_section.html'



class Delete_Subject(DeleteView):
    model = Subject
    success_url = 'dashboard'    
    template_name = 'delete_subject.html'
