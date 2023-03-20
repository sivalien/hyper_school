from django import forms

from .models import Student


class SearchForm(forms.Form):
    q = forms.CharField(label='search', required=False, max_length=32)


class StudentSignUpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'