from django import forms
from .models import Grade, Utilizator
from django.forms import TextInput, NumberInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.middleware import csrf

class MyModelForm(forms.ModelForm):
    course_name = forms.ModelChoiceField(queryset=Grade.objects.values_list('course_name', flat=True).distinct())
    class Meta:
        model = Grade
        fields = "__all__"


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['course_grade']
        widgets = {
            'course_grade': NumberInput(attrs={'placeholder': "Please insert the new grade"}),
        }

# class UserSignUpForm(forms.ModelForm):
class UserSignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Required.')
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, help_text='Required.',label='Parola')
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, help_text='Required.',label='Repetati parola')
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    is_teacher = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'is_teacher')

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if User.objects.filter(username=username).exists():
    #         raise forms.ValidationError("A user with that username already exists.")
    #     return username

    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.is_teacher = self.cleaned_data['is_teacher']
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
            Utilizator.objects.create(user=user, 
                                      first_name=user.first_name, 
                                      is_teacher=user.is_teacher,
                                      username=user.username,)
        return user

class UserLoginForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']
