from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Registerform, UserUpdate, ProfileUpdate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=="POST":
        form=Registerform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Successfully Account Created for {username}. Log In now!')
            return redirect('home')
    else:
        form=Registerform()
    return render(request,'auth/register.html',{'form':form})

@login_required
def profile(request):
    if request.method=="POST":
        u_form=UserUpdate(request.POST, instance=request.user)
        p_form=ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your account has been updated!')
            return redirect('profile')
    else:
        u_form=UserUpdate(instance=request.user)
        p_form=ProfileUpdate(instance=request.user.profile)

    context={'u_form':u_form, 'p_form':p_form}
    return render(request, 'auth/profile.html', context)