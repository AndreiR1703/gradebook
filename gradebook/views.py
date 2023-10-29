from django.shortcuts import render, redirect
from gradebook.models import Grade
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.contrib.auth import authenticate, login
# Create your views here.


def show_first_page(request):
    return render(request, template_name='home.html')


def show_grades(request):
    all_grades = Grade.objects.all
    grades_context = {"grades": all_grades}
    return render(request, template_name='gradebook/show_grades.html', context=grades_context)

def teacher_home(request):
    all_grades = Grade.objects.all
    grades_context = {"grades": all_grades}
    return render(request, template_name='gradebook/teacher.html', context=grades_context)

def pupil_home(request):
    all_grades = Grade.objects.all
    grades_context = {"grades": all_grades}
    return render(request, template_name='gradebook/pupil.html', context=grades_context)



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
    model = User
    template_name = "registration/signup.html"
    form_class = UserSignUpForm
    success_url = reverse_lazy("login")

class LogInView(View):
    model = User
    template_name = "registration/login.html"
    form_class = UserLoginForm


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_teacher:
                return redirect('teacher_home')
            else:
                return redirect('pupil_home')
        else:
            form = UserLoginForm()
            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(user.get_username())
                if user.is_teacher:
                    return redirect('teacher_home')
                else:
                    return redirect('pupil_home')
        return render(request, self.template_name, {'form': form})