"""
Views module
"""
from datetime import date
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView, ListView, TemplateView, CreateView
from .models import Employee
from .forms import SignupForm, AttendanceForm
import random
import string


# Create your views here.

class Home(TemplateView):
    """
    home page of the app
    """
    template_name = "kilimanjaro/home.html"

class UserSignup(FormView):
    """
    view to register a new user
    """
    template_name = "kilimanjaro/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        """
        creates an object in the Employee Table
        """
        user = form.save()
        Employee.objects.create(
            user = user,
            slug = user.username.join(random.choices(string.ascii_lowercase, k=5)),
            joined_at = date.today(),
        )
        return redirect(self.success_url)


class UserLogin(LoginView):
    """
    view for user to log in 
    """
    template_name = "kilimanjaro/login.html"
    next_page = "dashboard"


class Dashboard(ListView, LoginRequiredMixin):
    """
    view to display the dashboard of the employee
    """
    template_name = "kilimanjaro/dashboard.html"
    model = Employee
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = user.employee
        context['details'] = user.employee.get_employee_details()
        return context
    
class UserLogout(LogoutView):
    """
    view to logout user
    """
    next_page = reverse_lazy("home")


class AttendanceRecord(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    """
    view to display attendance record
    """
    template_name = "kilimanjaro/record.html"
    login_url = "login"
    model = Employee
    
    def has_permission(self) -> bool:
        return self.request.user.employee.is_authorized
    
    def get_queryset(self):
        """
        return all the employees
        """
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["record"] = self.model.get_attendance_record(context["object_list"])
        context["employee"] = self.request.user.employee
        print(self.request.user.employee.is_authorized)
        return context
    
class AttendanceView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    """
    view to display form to submit attendance
    """
    form_class = AttendanceForm
    template_name = "kilimanjaro/attendance.html"
    success_url = reverse_lazy("record")
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = self.request.user.employee
        return context
    