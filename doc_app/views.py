from django.shortcuts import render, redirect
from .models import Subject, Section
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import Subject_Form
from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin


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
    fields = ['intro','title']
    success_url = reverse_lazy('dashboard')  # Use reverse_lazy to avoid URL reversing issues

    def form_valid(self, form):
        # Set the author to the current user before saving the form
        form.instance.author = self.request.user
        return super().form_valid(form)




def Create_Subject(request, id):
    data = Section.objects.get(id=id)
    if request.method == 'POST':
        form = Subject_Form(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.section = data  # Assign the section to the subject
            myform.save()
            return redirect('/')
    else:
        form = Subject_Form()

    return render (request,'create_subject.html', {'form': form} )



class Update_Section(UpdateView):
    model = Section
    fields = '__all__'    
    template_name = 'update_form.html'
    success_url = '/'    


class Update_Subject(UpdateView):
    model = Subject
    fields = '__all__'    
    template_name = 'update_form.html'
    success_url = 'dashboard'    


class Delete_Section(DeleteView):
    model = Section
    success_url = '/'    
    template_name = 'delete_section.html'



class Delete_Subject(DeleteView):
    model = Subject
    success_url = '/'    
    template_name = 'delete_subject.html'
