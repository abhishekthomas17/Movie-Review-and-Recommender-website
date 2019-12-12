from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import profile
from django import forms
from movie.models import review,movie
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your views here.


class userregisterform(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','password1','password2']

def register(request):
    if request.method == "POST":
        forms=userregisterform(request.POST)
        if forms.is_valid():
            forms.save()
            username=forms.cleaned_data.get('username')
            messages.success(request,f'Account Created For {username}')
            return redirect('login')
    else:
        forms=userregisterform()

    return render(request,'register.html',{'form':forms})


class profileupdateform(forms.ModelForm):
    dob=forms.DateField(label="Date of Birth",help_text='Required. Format: YYYY-MM-DD')
    img=forms.ImageField(label="Profile picture")
    class Meta:
        model=profile
        fields=['firstname','lastname','email','dob','img']

@login_required
def profile_update_new(request):
    if request.method == "POST":
        forms=profileupdateform(request.POST,request.FILES,instance=request.user.profile)
        if forms.is_valid():
            forms.save()
            username=forms.cleaned_data.get('username')
            messages.success(request,f'Profile Updated For {request.user}')
            return redirect('profile_view')
    else:
        forms=profileupdateform(instance=request.user.profile)

    return render(request,'profile-update-new.html',{'form':forms})


@login_required
def profile_view(request):
    a = [i for i in review.objects.all() if i.user == request.user]

    return render(request,'profile-view.html',{'review':a})

def profile_view_user(request,pk):
    a=get_object_or_404(User,pk=pk)
    p=[i for i in profile.objects.all() if i.user == a]
    r=[i for i in review.objects.all() if i.user == a]

    return render(request,'profile-view-user.html',{'review':r,'profile':p,'a':a})
