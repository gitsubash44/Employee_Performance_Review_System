from django.shortcuts import render, redirect
from .models import CustomUser, UserTypes, PerformanceReview, Goal
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404


# Create your views here.
def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("password2")
        email = request.POST.get("email")
        user_type = request.POST.get('user_type')

        if password != confirm_password:
            messages.error(request, "password need to be same")
            return redirect('user_register')
        else:

            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "username already existed!")
                return redirect('user_register')
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, "email already taken")
                return redirect('user_register')
            else:
                # Create a new user
                user = CustomUser(
                    username=username,
                    email=email,
                    user_type=user_type
                )
                user.set_password(password)
                user.save()
                messages.success(request, "Account created successfully")
                return redirect('user_login')  

    return render(request, "registration/register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(user.user_type)

            login(request, user)
            # Redirect based on user type
            if user.user_type == UserTypes.EMPLOYER:
                return redirect('employee_dashboard')  
            elif user.user_type == UserTypes.MANAGER:
                return redirect('manager_dashboard')   
            elif user.user_type == UserTypes.INTERN:
                return redirect('intern_dashboard')    
            else:
                return redirect('homepage')
        else: 
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Please enter correct password")
            else:
                messages.error(request, "Invalid login credentials")
            return redirect('user_login')

    return render(request, "registration/login.html")



# manager 
def manager_dashboard(request):
    employees = CustomUser.objects.filter(user_type=UserTypes.EMPLOYER)
    interns = CustomUser.objects.filter(user_type=UserTypes.INTERN)
    context = {
        'employees': employees,
        'interns': interns,

    }
    return render(request, "manager/manager_dashboard.html", context)

def work_desc(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    # Fetching all performance reviews for the user
    performance_reviews = PerformanceReview.objects.filter(user=user).order_by("-id")[:3]

    if request.method =="POST":
        productivity_score = request.POST.get("productivity")
        punctuality_score = request.POST.get("punctuality")
        collaboration_score = request.POST.get("collaboration")
        goals = request.POST.get("goal")
        feedback = request.POST.get("feedbackText")

        try:
            performance_metrics = PerformanceReview.objects.create(
                user = user,
                productivity_score = productivity_score,
                punctuality_score = punctuality_score,
                collaboration_score = collaboration_score,
                goals = goals,
                feedback = feedback,
            )
            performance_metrics.save()
            messages.success(request, "Performance review saved successfully.")
        except ValueError as e:
            messages.error(request, f"Invalid input: {e}")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
        return redirect("work_desc", user_id=user.id)


    context = {
        'user': user,
        'performance_reviews': performance_reviews,

    }
    return render(request, "manager/work_desc.html", context)

# View performance details
def performance_details(request, review_id):
    review = get_object_or_404(PerformanceReview, id=review_id)


    data = {
        'review': review,

    }

    return render(request, "manager/performance_details.html", data)

# for viewing all review
def allReview(request, user_id):
    allReviews = PerformanceReview.objects.filter(user_id=user_id).order_by("-id")

    data={
        'allReviews': allReviews,
    }
    return render(request, "manager/allReview.html", data)

# For Assing Goals
def assign_goal(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        if description.strip():  # Ensure the description is not empty or just whitespace
            Goal.objects.create(description=description, status='in_progress', progress=0)
            messages.success(request, "Goal assigned successfully!")
        else:
            messages.error(request, "Goal description cannot be empty!")
        return redirect('assign_goal')  # Ensure this URL pattern is defined
    goals = Goal.objects.all()  # Fetch all goals to display
    return render(request, 'manager/Work_desc.html', {'goals': goals})

def UpCommingReview(request):
    return render(request, "manager/UpCommingReview.html")





# employer
def employer_dashboard(request):
    return render(request, "employer/employer_dashboard.html")


# intern
def intern_dashboard(request):
    return render(request, "intern/intern_dashboard.html")

def goals(request):
    # Query all goals from the database
    goals = Goal.objects.all()
    context = {
        'goals': Goal
    }
    return render(request, "intern/goals.html", context)


# intern
def employee_dashboard(request):
    return render(request, "intern/employee_dashboard.html")