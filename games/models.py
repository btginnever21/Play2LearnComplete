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


