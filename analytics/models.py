from django.db import models


class Theater(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)


class TicketSale(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_date = models.DateField()
    tickets_sold = models.IntegerField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)