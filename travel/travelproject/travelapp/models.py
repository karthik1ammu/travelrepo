from django.db import models

# Create your models here.
class place1(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class person(models.Model):
    pname = models.CharField(max_length=250)
    pimg = models.ImageField(upload_to='pics')
    pdesc = models.TextField()