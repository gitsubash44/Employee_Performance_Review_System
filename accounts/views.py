from django.shortcuts import render, redirect
from .models import CustomUser, UserTypes
from django.contrib import messages
from django.contrib.auth import authenticate, login




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
            print(user.user_type)  # Check what user type is being returned

            login(request, user)
            # Redirect based on user type
            if user.user_type == UserTypes.EMPLOYER:
                return redirect('employer_dashboard')  
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

def work_desc(request):
    return render(request, "manager/work_desc.html")


# employer
def employer_dashboard(request):
    return render(request, "employer/employer_dashboard.html")



# intern
def intern_dashboard(request):
    return render(request, "intern/intern_dashboard.html")