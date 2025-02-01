from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    author_name = models.CharField(max_length=100)



class BookList(models.Model):
    name = models.CharField(max_length=500)
    books = models.ManyToManyField(Book)

