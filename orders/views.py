from django.shortcuts import render, redirect
from django.contrib import messages

from orders.models import Employee
from .forms import AddEmployeeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import ForgotPasswordForm
from .forms import AddEmployeeForm
from django.http import JsonResponse




def homepage(request):
    form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            # Redirect based on role
            if user.role == 'admin':
                return redirect('adminPage')  # Update this with your admin dashboard URL
            elif user.role == 'manager':
                return redirect('manager_dashboard')  # Define URLs for managers
            else:
                return redirect('employee_dashboard')  # Define URLs for employees

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def forgotPwd(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            # Handle the form submission here (send reset email, etc.)
            pass
    else:
        form = ForgotPasswordForm()
    
    return render(request, 'forgotPwd.html', {'form': form})

def adminPage(request):
    form = AddEmployeeForm()
    
    if request.method == "POST":
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to some success page or reload the admin page
    return render(request, 'Admin.html', {'form': form})


def employee(request):
     return render(request, 'clockIn.html')

def forgotPwd(request):
     return render(request, 'forgotPwd.html')

def adminPage(request):
     return render(request, 'Admin.html')



from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

def add_employee_view(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])  # Hash the password
                user.save()

                # Create and save the Employee object
                Employee.objects.create(
                    user=user,
                    name=form.cleaned_data['first_name'],  # Fixed to use first_name
                    surname=form.cleaned_data['last_name'],  # Fixed to use last_name
                    role=form.cleaned_data['role'],
                    gender=form.cleaned_data['gender'],
                    age=form.cleaned_data['age'],
                    phone=form.cleaned_data['phone'],
                    email=form.cleaned_data['email'],
                )

                # Return a success response in JSON format
                return JsonResponse({'success': True})

            except Exception as e:
                # Return an error response in JSON format
                return JsonResponse({'success': False, 'error': str(e)}, status=500)
        else:
            # Return form validation errors
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    
    else:
        form = AddEmployeeForm()

    return render(request, 'Admin.html', {'form': form})