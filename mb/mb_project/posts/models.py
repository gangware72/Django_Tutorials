from django.db import models #models the characteristics of the data in our database

class Post(models.Model):
    text = models.TextField() #specified the type of content the field will hold
    def __str__(self):
        return self.text[:50]

#
# Create your models here.
