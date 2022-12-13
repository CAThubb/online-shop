from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Language(models.Model):
    language_id = models.IntegerField(primary_key=True)
    language = models.CharField(max_length=15)

    def __str__(self):
        return self.language


class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre


class Author(models.Model):
    auth_id = models.IntegerField(primary_key=True)
    FSL_name = models.CharField(max_length=150)

    def __str__(self):
        return self.FSL_name


class PublishingHouse(models.Model):
    house_id = models.IntegerField(primary_key=True)
    house_name = models.CharField(max_length=10)

    def __str__(self):
        return self.house_name

class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    pages_quantity = models.IntegerField()
    year_of_publishing = models.DateField()

    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)
    phouse_name = models.ManyToManyField(PublishingHouse)

    def __str__(self):
        return self.title
