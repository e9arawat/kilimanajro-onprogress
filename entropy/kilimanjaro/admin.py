"""
Admin Panel view
"""
from django.contrib import admin
from .models import Employee, Attendance

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    displays the employee model on the admin panel
    """
    list_display = ["user", "joined_at", "role", "manager", "earned_leaves", "is_authorized"]


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    """
    displays the attendance model on the admin panel
    """
    list_display = ["employee", "date", "status"]