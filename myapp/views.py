from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .form import RegisterUserForm


#register recruiter 
def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_recruiter = True
            user.username = user.email
            user.save()
            messages.success(request, 'Your account has been created successfully. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Something went wrong. Please correct the errors below.')
    else:
        form = RegisterUserForm()
    
    context = {'form': form}
    return render(request, 'users/register_recruiter.html', context)

#login user
def login_user(request):
    if request.method == 'POST':
        email= request.POST.get('email')
        password = request.POST.get('password')

        user =authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.warning(request,"Something went wrong")
            return redirect('login')
    else:
        return render(request,'users/login.html')
    
#logout a user
def logout_user(request):
    logout(request)
    messages.info(request,'Your session has ended')
    return redirect('login')

