from django.http import request, response 
from django.shortcuts import render , redirect


def home(request):
    return render(request,"index.html")





from django.contrib.auth import authenticate, login
from django.contrib import messages

def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'dashboard.html')  # Redirect to doctor's dashboard or profile page
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'index.html')
def graph(request):
    return render(request,"graph.html")