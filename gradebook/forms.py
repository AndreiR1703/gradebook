from django import forms
from .models import Grade
from django.forms import TextInput, NumberInput

class MyModelForm(forms.ModelForm):
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



