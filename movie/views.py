from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import movie,review
from django import forms
from django.shortcuts import get_object_or_404
from django.contrib import messages

from user_sim import *
import pickle
import csv

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import CreateView,UpdateView,DeleteView
# Create your views here.

def home(request):
    a=[i for i in movie.objects.all()]
    context={"mov":a,"r":range(0,10)}
    return render(request,"home.html",context)


class moviereviewform(forms.ModelForm):
    review_text=forms.CharField(widget=forms.Textarea,label="Write review")
    rating=forms.FloatField(label="Give your rating")
    class Meta:
        model=review
        fields=['review_text','rating']


def view_movie(request,pk):
    a=get_object_or_404(movie,pk=pk)
    b=[i for i in review.objects.all() if i.review_movie==a]
    return render(request,'view-movie.html',{"m":a,"r":b})

@login_required
def write_review(request,pk):
    a=get_object_or_404(movie,pk=pk)
    if request.method=="POST":
        form=moviereviewform(request.POST,request.FILES)
        form.instance.review_movie=a
        form.instance.user=request.user
        if form.is_valid():
            form.save()
            m=a.title
            messages.success(request,f'Review Writtern For {m}')
            return redirect('view_movie',a.id)
    else:
        form=moviereviewform()

    return render(request,'write-review.html',{"form":form,"b":a})

def update_review(request,pk,pk1):
    a=get_object_or_404(movie,pk=pk)
    b=get_object_or_404(review,pk=pk1)

    if request.method=="POST":
        form=moviereviewform(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
            m=a.title
            messages.success(request,f'Review Updated For {m}')
            return redirect('view_movie',a.id)
    else:
        form=moviereviewform(instance=b)

    return render(request,'write-review.html',{"form":form,"b":a})


def delete_review(request,pk,pk1):
    a=get_object_or_404(movie,pk=pk)
    b=get_object_or_404(review,pk=pk1)

    if request.method=="POST":
        q=review.objects.get(pk=pk1)
        q.delete()
        return redirect('view_movie',a.id)

    return render(request,'delete-review.html',{"b":a})

def search_movie_genre(request):
    a=[i.genre for i in movie.objects.all()]

    b=list(set(a))

    return render(request,'search-movie-genre.html',{'genre':b})

def searched_movie_genre(request):
    if request.method == 'GET':
        search_query = request.GET.get('select_box', None)

    a=[i for i in movie.objects.all() if search_query in i.genre]

    return render(request,'searched-movie-genre.html',{'movie':a,"s":search_query})

def search_movie_name(request):

    return render(request,'search-movie-name.html')

def searched_movie_name(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)
        if len(search_query)==0:
            messages.success(request,f'Please Enter Value To Search')
            return redirect('search_movie_name')


    a=[i for i in movie.objects.all() if search_query.lower() in (i.title)]
    len1=len(a)

    return render(request,'searched-movie-name.html',{'movie':a,'l':len1})

selected={}
def movie_recommender(request):
    movies={}
    global selected
    with open("movies.pickle","rb") as file:
        movies=pickle.load(file)
    if request.GET.get('movie'):
        search_query1 = request.GET.get('movie', None)
        search_query2 = request.GET.get('rating', None)
        if len(search_query1)==0:
            messages.warning(request,'Please Enter Value')
            return redirect('movie_recommender')

        elif len(search_query2)==0:
            messages.warning(request,'Please Enter Value')
            return redirect('movie_recommender')
        selected[search_query1]=float(search_query2)
    if request.GET.get('submit2'):
        if(len(selected)<2):
            messages.success(request,'Please Select Atleast 2 Movies')
            return redirect('movie_recommender')
        else:
            return redirect('movie_recommender_done')
    if request.GET.get('submit3'):
        if(len(selected)<2):
            messages.success(request,'Please Select Atleast 2 Movies')
            return redirect('movie_recommender')
        else:
            return redirect('movie_recommender_done')
    if request.GET.get('clear'):
        selected={}

    return render(request,'movie-recommender.html',{"movies":movies,"s":selected})


def movie_recommender_done(request):
    global selected
    a=selected

    l=recommender(a)

    if request.GET.get('back'):
        selected={}
        return redirect('movie_recommender')

    return render(request,'movie-recommender-done.html',{"s":a,"list":l,"u":user_rating})

def movie_recommender_done1(request):
    global selected
    a=selected

    l=recommender1(a)
    if request.GET.get('back'):
        selected={}
        return redirect('movie_recommender')

    return render(request,'movie-recommender-done.html',{"s":a,"list":l,"u":user_rating})
