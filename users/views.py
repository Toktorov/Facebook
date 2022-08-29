from django.shortcuts import render, redirect
from users.models import User
from django.contrib.auth import login, authenticate

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profile_image = request.FILES.get('profile_image')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create(username = username, last_name = last_name, first_name = first_name, email = email, phone = phone, profile_image = profile_image)
            user.set_password(password)
            user.save()
            return redirect('index')
        else:
            return redirect('register')

    return render(request, 'register.html')