from django.db import models

# Create your models here.

class Friends(models.Model):
    fname=models.CharField(max_length=100)
    fnum=models.IntegerField()
    fmail=models.CharField(max_length=50)
    floc=models.CharField(max_length=100)

    def __str__(self):
        return self.fname
