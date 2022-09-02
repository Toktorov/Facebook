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
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
        else:
            return redirect('register')
    return render(request, 'register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username = username)
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('index')
    return render(request, 'login.html')

def user_detail(request, id):
    user = User.objects.get(id = id)
    context = {
        'user' : user,
    }
    return render(request, 'user_detail.html', context)

def user_update(request, id):
    user = User.objects.get(id = id)
    if request.method == "POST":
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profile_image = request.FILES.get('profile_image')
        user = User.objects.get(id = id)
        user.username = username 
        user.last_name = last_name
        user.first_name = first_name
        user.email = email 
        user.phone = phone 
        user.profile_image = profile_image
        user.save()
        return redirect('user_detail', user.id)
    context = {
        'user' : user,
    }
    return render(request, 'user_update.html', context)

def user_delete(request, id):
    user = User.objects.get(id = id)
    if request.method == "POST":
        user = User.objects.get(id = id)
        user.delete()
        return redirect('index')
    context = {
        'user' : user,
    }
    return render(request, 'user_delete.html', context)