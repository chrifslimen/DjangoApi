from django.db import models

# Create your models here.
class Artical(models.Model):
    title = models.CharField(max_length=100)
    auth = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class compte(models.Model):
    userName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email

def uploadPath(instance, filename):
    return '/'.join(['Images', filename])
class Photo (models.Model):
    #email = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to=uploadPath)
    date = models.DateTimeField(auto_now_add=True)
    #syndrom = models.CharField(max_length=100)
    def __str__(self):
        return str(self.date)
