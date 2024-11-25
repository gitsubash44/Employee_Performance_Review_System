from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
    path('',views.user_login, name="user_login"),
    path('register/',views.user_register, name="user_register"),


    #manager
    path('manager_dashboard/', views.manager_dashboard, name="manager_dashboard"),
    path('work_desc/<int:user_id>/', views.work_desc, name='work_desc'),
    path('performance_details/<int:review_id>/', views.performance_details, name='performance_details'),
    path('reviews/<int:user_id>', views.allReview, name='all_reviews'),

    

    # employer
    path('employer_dashboard/', views.employer_dashboard, name="employer_dashboard"),

    # Intern
    path('intern_dashboard/', views.intern_dashboard, name="intern_dashboard"),
    path('goals/', views.goals, name="goals"),
    
    # Employees 
    path('employee_dashboard/', views.employee_dashboard, name="employee_dashboard"),
    

]