from django.db import models

# Create your models here.
class Posts(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=20, unique=True)
    content = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=500)
    phone = models.IntegerField(max_length=15)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name