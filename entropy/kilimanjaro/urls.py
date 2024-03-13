"""
URL module
"""
from django.urls import path
from kilimanjaro import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("signup/", views.UserSignup.as_view(), name="signup"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
    path("logout/", views.UserLogout.as_view(), name="logout"),
    path("record/", views.AttendanceRecord.as_view(), name="record"),
    path("attendance/", views.AttendanceView.as_view(), name="attendance"),
    
]