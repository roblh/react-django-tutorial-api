from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Lesson Before project Django project needs to be added to settings.py
# Lesson create user with 
# Lesson - Every change to model needs migrations with python3 managepy makemigrations


# Create your models here.

class Movie(models.Model): #Lesson, these 
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def no_of_ratings(self): 
        #In order to pass in a custom method, 
        #just need to define it under the model here and make sure it gets included in the serializer
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

class Rating (models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),
    MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)