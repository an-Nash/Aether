from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(primary_key=True, unique=True, max_length=200)
    email = models.EmailField(max_length=150)
    name = models.CharField(max_length=200)
    match = models.ManyToManyField("self",blank=True,symmetrical=False, related_name="matched")
    like = models.ManyToManyField("self",blank=True, related_name="liking", symmetrical=False)
    age = models.IntegerField(blank=False)
    profession = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    working_instituition = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    state = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.username}'