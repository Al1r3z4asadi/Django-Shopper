from django.shortcuts import render , redirect
from .form import UserRegisterForm , UserUpdateForm  , ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.models import User



def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , f'اکانت برای   {username} ساخته شد .!')
            return redirect('shop:shopper-home')
    else:
        form = UserRegisterForm()
    
    
    
    context = {
        'form' : form 
    }
    return render(request , 'user/register.html', context )



@login_required
def profile(request , name ):
    print("name is " , name)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST , instance=request.user)
        print("let se what are the request.FILES" , request.FILES)
        p_form = ProfileUpdateForm(request.POST ,request.FILES , instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request , f'your account has been updated !')
            return redirect('profile',name=request.user.username)          
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context={
        'name' : User.objects.get(username=name),
        'u_form' : u_form,
        'p_form' : p_form
    }
    
    
    return render(request , 'user/profile.html' ,context )

    