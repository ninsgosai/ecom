from django.shortcuts import render,redirect,HttpResponse
from .models import user
from product.models import product
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == "POST":
        if user.objects.filter(email=request.POST['email']).exists():
            if user.objects.filter(email=request.POST['email'],password=request.POST['password']).exists():
                user_id = user.objects.get(email=request.POST['email'])
                request.session['user_id'] = user_id.pk
                return redirect('products')
            else:
                messages.add_message(request,messages.ERROR,"Userid & Password are not matched")
        else:
            messages.add_message(request,messages.ERROR,"Email isn't Registered")

    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        if user.objects.filter(email=request.POST['email']).exists():
            messages.add_message(request,messages.ERROR,'Email is already Registerd')
        else:
            new_user = user()
            new_user.name = request.POST['name']
            new_user.email = request.POST['email']
            new_user.password = request.POST['password']
            new_user.confirm_password = request.POST['confirm_password']
            new_user.image = request.FILES['profile_pic']
            new_user.save()
            return redirect('products')
    return render(request,'register.html')

def logout(request):
    del request.session['user_id']
    return redirect('home')