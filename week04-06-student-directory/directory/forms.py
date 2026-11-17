from django import forms
from .models import Student

class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "age", "email", "enrolment_date", "modules", "image"]
        widgets = {"enrolment_date": forms.DateInput(attrs={"type": "date"})}

class StudentFilterForm(forms.Form):
    first_name = forms.CharField(required=False, label="First name contains")
    last_name = forms.CharField(required=False, label="Last name contains")
    module = forms.CharField(required=False, label="Module code contains")
