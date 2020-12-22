from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=256)
    length = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()
    def __Str__(self):  #if no these codes, then when you create an example in this table, in admin page it will show as 'Movie object',
        return self.title # Now it will show as 'title'

class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name+ ' '+ self.last_name
