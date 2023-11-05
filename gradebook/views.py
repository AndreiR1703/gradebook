from django.shortcuts import render, redirect
from gradebook.models import Grade, Utilizator
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.contrib.auth import authenticate, login
# Create your views here.


global is_professor

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
    success_url = reverse_lazy('teacher-page')
    
    def get_form_kwargs(self):
        kwargs = super(GradeCreateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

class GradeUpdateView(UpdateView):
    model = Grade
    template_name = 'gradebook/form.html'
    form_class = UpdateForm
    success_url = reverse_lazy('teacher-page')

class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'gradebook/deleteform.html'
    success_url = reverse_lazy('teacher-page')


class SignUpView(CreateView):
    model = User
    template_name = "registration/signup.html"
    form_class = UserSignUpForm
    success_url = reverse_lazy("login")
    
from django.contrib.auth.backends import ModelBackend

class LogInView(View):
    model = User
    template_name = "registration/login.html"
    form_class = UserLoginForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print("got form")

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f"username={username}, password={password}")
            try:
                user = self.model.objects.get(username=username)
                user.backend = f"{ModelBackend.__module__}.{ModelBackend.__qualname__}"
                if user.check_password(password):

                    login(request, user)
                    print(f"User {user} logged in")
                    if user.username == 'admin':
                        return redirect('teacher-page')
                    elif user.utilizator.is_teacher:
                        return redirect('teacher-page')
                    else:
                        return redirect('pupil-page')
                else:
                    form.add_error(None, "Invalid username or password")
                    print("Invalid username or password")
            except User.DoesNotExist:
                form.add_error(None, "Invalid username or password")
                print("Invalid username or password")
        else:
            print(f"Form is not valid {form.errors}")
        return render(request, self.template_name, {'form': form})