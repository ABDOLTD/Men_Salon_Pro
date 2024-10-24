from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def make_appointment(request):
    return render(request, 'make_appointment.html')

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')
