from django.db import models
from django.urls import reverse


# Create your models here.
class GameScore(models.Model):

    MATH="MATH"
    ANAGRAM="ANAGRAM"

    GAME_CHOICES = [
        (MATH, "MathGame"),
        (ANAGRAM, "AnagramGame")
    ]
    user_name = models.TextField()
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    Review = models.TextField(max_length=200)
    Username = models.TextField(max_length=20, blank=True)
    def get_absolute_url(self):
        return reverse('joke', args=[self.slug])
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('reviews:detail', args=[str(self.pk)])


    def __str__(self):
        return self.question