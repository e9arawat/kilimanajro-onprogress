"""
Form module
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Attendance

class SignupForm(UserCreationForm):
    """
    form to register a new user
    """
    class Meta:
        """
        Meta class
        """
        model = get_user_model()
        fields = ["username", "first_name", "last_name", "email"]


class AttendanceForm(forms.ModelForm):
    """
    form to add attendance
    """
    class Meta:
        """
        Meta class
        """
        model = Attendance
        fields = [ "date", "employee", "status"]

        widgets = {
            "date" : forms.DateInput(attrs={"class":"form-control", "type":"date"}),
            "employee" : forms.Select(attrs={"class":"form-control"}),
            "status" : forms.Select(attrs={"class":"form-control"}),
        }