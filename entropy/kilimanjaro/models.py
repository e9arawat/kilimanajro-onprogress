"""
Model module
"""
from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from django.db.models import Q


class Employee(models.Model):
    """
    Employee model
    """
    role_choices = [
        ("Trainee", "Trainee"),
        ("Developer", "Developer"),
        ("HR", "HR"),
        ("Analyst", "Analyst"),
    ]
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="employee")
    slug = models.CharField(max_length=50)
    joined_at = models.DateField()
    role = models.CharField(max_length=50, choices=role_choices, default="Trainee")
    manager = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="employee")
    earned_leaves = models.IntegerField(default=24)
    is_authorized = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.get_full_name()}"

    @classmethod
    def get_attendance_record(cls, employees):
        """
        return the attendance record of all the employees
        """
        return [employee.get_employee_details() for employee in employees]

    
    @classmethod
    def find_start_date(cls):
        """
        return the minimum date
        """
        all_dates_object = cls.objects.all().values("start_date")
        if not all_dates_object:
            return []
        all_dates = [x["start_date"] for x in all_dates_object]
        return min(all_dates)

    def get_employee_details(self):
        """
        return the details of the employee
        """
        total_days = (date.today() - self.joined_at).days + 1
        total_leaves = self.attendance.filter(Q(status="Sick") | Q(status="Absent") | Q(status="Vacation")).count()
        absent = self.attendance.filter(status="Absent").count()
        sick = self.attendance.filter(status="Sick").count()
        vacation = self.attendance.filter(status="Vacation").count()
        late = self.attendance.filter(status="Late").count()
        absent += int(late/3)
        attendance_percentage = round(((total_days - absent)/total_days)*100, 2) if total_days > 0 else 0
        travel = self.attendance.filter(status="Travel").count()

        details = {
            "Name" : self.user.get_full_name(),
            "Joined_at" : self.joined_at,
            "Role" : self.role,
            "Manager" : self.manager,
            "Earned_Leaves" : self.earned_leaves,
            "Leaves" :  total_leaves,
            "Travels" : travel,
            "Attendance" : attendance_percentage,
            "Leaves_category" : f"Sick = {sick}, Vacation = {vacation}, Late = {int(late/3)}"
        }
        return details


    
    def get_date_attendance(cls, date_param, employees):
        """
        return the attendance record of the searched date (date_param) for all the employees
        """
        return 
    
    def get_all_dates_attendance(cls, employees):
        """
        return the attendance record of all the employees for each date
        """
        return 
    

class Attendance(models.Model):
    """
    Attendance model
    """
    status_choices = [
        ("Absent", "Absent"),
        ("Late", "Late"),
        ("Sick", "Sick"),
        ("Travel", "Travel"),
        ("Vacation", "Vacation"),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField()
    status = models.CharField(max_length=50, choices=status_choices)

    class Meta:
        """
        Meta class
        """
        unique_together = ["employee", "date"]

