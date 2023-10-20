from django.db import models


class Ratings(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default="", blank=True)
    rating = models.CharField(
        max_length=20,
        choices=Ratings.choices,
        default=Ratings.G,
    )
    synopsis = models.TextField(default="", blank=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movie",
    )
    movies_orders = models.ManyToManyField(
        "users.User",
        related_name="order",
        through="movies_orders.MovieOrder",
    )
