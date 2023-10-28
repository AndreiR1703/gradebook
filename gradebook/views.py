from django.shortcuts import render
from gradebook.models import Grade
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView
# Create your views here.


def show_first_page(request):
    return render(request, template_name='home.html')


def show_grades(request):
    all_grades = Grade.objects.all
    grades_context = {"grades": all_grades}
    return render(request, template_name='gradebook/show_grades.html', context=grades_context)


class GradeCreateView(CreateView):
    model = Grade
    template_name = 'gradebook/form.html'
    form_class = MyModelForm
    success_url = reverse_lazy('show-grades')

class GradeUpdateView(UpdateView):
    model = Grade
    template_name = 'gradebook/form.html'
    form_class = UpdateForm
    success_url = reverse_lazy('show-grades')

class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'gradebook/deleteform.html'
    success_url = reverse_lazy('show-grades')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"