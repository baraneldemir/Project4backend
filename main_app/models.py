from django.db import models
from django.urls import reverse

# Create your models here.


class Cat(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    twitter = models.TextField(max_length=250)
    linkedin = models.TextField(max_length=250)
    image = models.TextField(max_length=250)
    
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'people_id': self.id})



class Photo(models.Model):
    url = models.CharField(max_length=200)
    people = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for people_id: {self.people_id} @ {self.url}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'people_id': self.id})



# class Comment(models.Model):
#     comment_owner = models.CharField(max_length=50)
#     comment = models.TextField(max_length=500)


#     def __str__(self):
#         return self.name    

