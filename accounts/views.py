from django.shortcuts import render, redirect
from .models import CustomUser, UserTypes, PerformanceReview, Goal, ReviewScheduling, Review
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.utils.timezone import now




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
                return redirect('intern_dashboard', user_id=user.id)    
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
    
    # print(request.user.user_type)
    context = {
        'employees': employees,
        'interns': interns,
        'user': request.user

    }
    return render(request, "manager/manager_dashboard.html", context)

def work_desc(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    # Fetching all performance reviews for the user
    performance_reviews = PerformanceReview.objects.filter(user=user).order_by("-id")[:3]
    upcoming_reviews = ReviewScheduling.objects.filter(user=user).order_by("-id")[:3]
    assigned_goals = Goal.objects.filter(assigned_to=user).order_by("-id")[:5]


    if "savePerformance" in request.POST:
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
    
# Handle Review Scheduling Form submission
    if "scheduleReview" in request.POST:  # Check if this is the review scheduling form
        review_title = request.POST.get("reviewTitle")
        review_date = request.POST.get("reviewDate")
        review_time = request.POST.get("reviewTime")

        try:
            upcoming_review = ReviewScheduling.objects.create(
                user=user,
                review_title=review_title,
                review_date=datetime.strptime(review_date, "%Y-%m-%d").date(),
                review_time=datetime.strptime(review_time, "%H:%M").time()
            )
            upcoming_review.save()
            messages.success(request, "Review scheduled successfully.")
        except Exception as e:
            messages.error(request, f"Error in scheduling review: {e}")

    context = {
        'user': user,
        'performance_reviews': performance_reviews,
        'upcoming_reviews': upcoming_reviews,
        'assigned_goals': assigned_goals,

    }
    return render(request, "manager/work_desc.html", context)

# View performance details
def performance_details(request, review_id):
    review = get_object_or_404(PerformanceReview, id=review_id)
    user = review.user  # The user associated with the review



    data = {
        'review': review,
        'user': user,

    }

    return render(request, "manager/performance_details.html", data)

# for viewing all review
def allReview(request, user_id):
    allReviews = PerformanceReview.objects.filter(user_id=user_id).order_by("-id")

    data={
        'allReviews': allReviews,
    }
    return render(request, "manager/allReview.html", data)

def assign_goal(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)  # Get the user object
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')

        if title.strip() and description.strip():  # Ensure title and description are not empty
            Goal.objects.create(
                title=title,
                description=description,
                status='in_progress',
                progress=0,
                deadline=deadline if deadline else None,  # Set deadline if provided
                assigned_to=user  # Link the goal to the user
            )
            messages.success(request, "Goal assigned successfully!")
        else:
            messages.error(request, "Goal title and description cannot be empty!")

    goals = Goal.objects.filter(assigned_to=user)  # Get goals assigned to this user
    data = {
        'goals': goals,
        'user': user,  # Pass the user object to the template
    }
    return render(request, 'manager/Work_desc.html', data)

def UpCommingReview(request):
    return render(request, "manager/UpCommingReview.html")



# employer
def employer_dashboard(request):
    return render(request, "employer/employer_dashboard.html")


# intern
def intern_dashboard(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    performance_reviews = PerformanceReview.objects.filter(user=user).order_by("-id")[:3]

    data = {
        'user': user,
        'performance_reviews': performance_reviews,
        }

    return render(request, "intern/intern_dashboard.html", data)

def intern_performance_details(request, review_id):
    review = get_object_or_404(PerformanceReview, id=review_id)
    user = review.user  



    data = {
        'review': review,
        'user': user,

    }

    return render(request, "intern/intern_performance_detail.html", data)


def Self_Assessment(request):
    return render(request, "intern/Self_Assessment.html")

def goals(request):
    user = request.user  # Get the currently logged-in user

    # Update missed status for goals whose deadlines have passed and are not achieved
    for goal in Goal.objects.filter(assigned_to=user):  # Filter goals by the logged-in user
        if goal.deadline and now() > goal.deadline and goal.status != "achieved":
            goal.status = "missed"
            goal.save()

    # Retrieve the latest 3 goals assigned to the current user
    goals = Goal.objects.filter(assigned_to=user).order_by("-id")[:3]

    context = {
        'goals': goals
    }
    return render(request, "intern/goals.html", context)

def assign_goals(request):
# Fetch only interns or specific user types
    users = CustomUser.objects.filter(user_type=UserTypes.INTERN)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        assigned_to_id = request.POST.get('assigned_to')

        # Check if all necessary fields are provided
        if not title or not description or not deadline or not assigned_to_id:
            messages.error(request, "All fields are required.")
            return redirect('assign_goal')  # Adjust URL name if needed

        try:
            assigned_to = CustomUser.objects.get(id=assigned_to_id)

            # Create and save the goal
            Goal.objects.create(
                title=title,
                description=description,
                deadline=deadline,
                assigned_to=assigned_to
            )
            messages.success(request, f"Goal '{title}' has been assigned to {assigned_to.username}.")
            return redirect('assign_goal')  # Adjust URL name if needed

        except CustomUser.DoesNotExist:
            messages.error(request, "Invalid user selected.")
            return redirect('assign_goal')

    context = {
        'users': users
    }
    return render(request, "manager/work_desc.html", context)





def goals_history(request):
    user = request.user  # Get the currently logged-in user

    if request.method == "POST":
        goal_id = request.POST.get("goal_id")
        action = request.POST.get("action")
        goal = get_object_or_404(Goal, id=goal_id)

        if action == "complete":
            goal.status = "achieved"
            goal.completed = True
            goal.save()

    # Update missed status for goals past their deadline
    for goal in Goal.objects.all():
        if goal.deadline and now() > goal.deadline and goal.status != "achieved":
            goal.status = "missed"
            goal.save()

    goals = Goal.objects.filter(assigned_to=user).order_by("-id")
    context = {"goals": goals}
    return render(request, "intern/goals_history.html", context)

# intern
def employee_dashboard(request):
    return render(request, "intern/employee_dashboard.html")



# For Logout
def logout_view(request):
    """
    Logs out the user and redirects to the homepage.
    """
    logout(request)
    return redirect('/')  # Redirect to the homepage or login page


def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    
    if request.method == "POST":
        # Get the data from the request
        productivity_score = request.POST.get("productivity_score")
        punctuality_score = request.POST.get("punctuality_score")
        collaboration_score = request.POST.get("collaboration_score")
        goals = request.POST.get("goals")
        feedback = request.POST.get("feedback")

        # Update the review instance
        review.productivity_score = productivity_score
        review.punctuality_score = punctuality_score
        review.collaboration_score = collaboration_score
        review.goals = goals
        review.feedback = feedback

        # Save the changes to the database
        review.save()

        # Redirect back to the details page or list
        return redirect('work_desc', review.user.id)

    # Render the same template with review details
    return render(request, "edit_review.html", {"review": review})