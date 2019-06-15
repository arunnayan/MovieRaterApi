from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)



class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) #models.CASCADE is used when movie is deleted then there is no rating required
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    class Meta:
        unique_together = (('user','movie'),) # a user can give rating to movie one time
        index_together = (('user','movie'),)
