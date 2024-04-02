from django.db import models
from auth_app.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    release_date = models.DateField()

    def __str__(self):
        return self.name


class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='ratings')
    rating = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(5.0)] )

    class Meta:
        unique_together = ('user_id', 'movie_id')

    def __str__(self):
        return f"Rating for {self.movie_id.name} by {self.user_id.name}"
