from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class movie(models.Model):
    title=models.CharField(max_length=100)
    director=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    imdb_rating=models.FloatField(default=0,validators=[MaxValueValidator(10),MinValueValidator(0)])
    avg_user_rating=models.FloatField(default=0,validators=[MaxValueValidator(10),MinValueValidator(0)])
    year=models.CharField(max_length=15)
    review_mov=models.TextField()
    img=models.ImageField(default="none.jpg",upload_to="movie_pics")

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.title=self.title.lower()
        return super(movie,self).save(*args,**kwargs)


class review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    review_movie=models.ForeignKey(movie,on_delete=models.CASCADE)
    review_text=models.TextField()
    rating=models.FloatField(default=0,validators=[MaxValueValidator(10),MinValueValidator(0)])


    def __str__(self):
        return self.review_movie.title
