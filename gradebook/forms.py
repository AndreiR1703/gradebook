from django import forms
from .models import Grade, User
from django.forms import TextInput, NumberInput

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

class UserSignUpForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = "__all__"

    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
