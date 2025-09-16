from django.db import models

from .constant import NAME_MAX_LENGTH


class Country(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH['country'])

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH['manufacturer'])
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='manufacturers')

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH['car'])
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name='cars')
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author_email = models.EmailField()
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.text
