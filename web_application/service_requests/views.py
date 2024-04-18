from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import ServiceRequestForm, UserRegistrationForm
from .models import ServiceRequest

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('submit_success')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def track_requests(request):
    service_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'track_requests.html', {'service_requests': service_requests})

def submit_success(request):
    return render(request, 'submit_success.html')
# def track_requests(request):
#     # Check if the user is an administrator
#     if request.user.username == 'admin':
#         # Authenticate the user with the provided password
#         user = authenticate(username='admin', password='admin@123')
#         if user is not None:
#             # User is authenticated as admin, fetch service requests
#             service_requests = ServiceRequest.objects.filter(user=request.user)
#             return render(request, 'track_requests.html', {'service_requests': service_requests})
#         else:
#             # Invalid credentials for admin, redirect to submit_request.html
#             return redirect('submit_request')
#     else:
#         # User is not an administrator, redirect to submit_request.html
#         return redirect('submit_request')
