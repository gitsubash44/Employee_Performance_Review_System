from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
    path('register/',views.user_register, name="user_register"),
    path('login/',views.user_login, name="user_login"),


    #manager
    path('manager_dashboard/', views.manager_dashboard, name="manager_dashboard"),

    # employer
    path('employer_dashboard/', views.employer_dashboard, name="employer_dashboard"),

    # Intern
    path('intern_dashboard/', views.intern_dashboard, name="intern_dashboard"),

]