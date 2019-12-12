"""movie_review URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie import views
from user import views as uviews
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="logout.html"),name='logout'),
    path('register/',uviews.register,name='register'),

    path('password-reset/',
    auth_views.PasswordResetView.as_view(template_name="password-reset.html")
    ,name='password_reset'),

    path('password-reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name="password-reset-done.html")
    ,name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>',
    auth_views.PasswordResetConfirmView.as_view(template_name="password-reset-confirm.html")
    ,name='password_reset_confirm'),

    path('password-reset-complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name="password-reset-complete.html")
    ,name='password_reset_complete'),

    path('profile-update',uviews.profile_update_new,name='profile_update_new'),
    path('profile-view',uviews.profile_view,name='profile_view'),
    path('profile-view/<int:pk>',uviews.profile_view_user,name='profile_view_user'),
    path('view-movie/<int:pk>',views.view_movie,name='view_movie'),
    path('view-movie/<int:pk>/write-review',views.write_review,name='write_review'),
    path('view-movie/<int:pk>/update-review/<int:pk1>',views.update_review,name='update_review'),
    path('view-movie/<int:pk>/delete-review/<int:pk1>',views.delete_review,name='delete_review'),
    path('search-movie-genre/',views.search_movie_genre,name='search_movie_genre'),
    path('searched-by-genre/',views.searched_movie_genre,name='searched_movie_genre'),
    path('search-movie-name/',views.search_movie_name,name='search_movie_name'),
    path('searched-by-name/',views.searched_movie_name,name='searched_movie_name'),
    path('movie-recommender/',views.movie_recommender,name='movie_recommender'),
    path('movie-recommender-done/users',views.movie_recommender_done,name='movie_recommender_done'),
    path('movie-recommender-done/items',views.movie_recommender_done1,name='movie_recommender_done1'),



]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.MEDIA_URL1,document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.MEDIA_URL2,document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.MEDIA_URL3,document_root=settings.MEDIA_ROOT)
