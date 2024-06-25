from django.db import models
from django.utils import timezone
#to set auter i.e user from user table we need to add
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class post (models.Model):
    title = models.CharField(max_length=100)
    contact =models.TextField()
    date_pasted = models.DateTimeField(default=timezone.now)#possible value
    #need author have a relation with user table in django database
    author =models.ForeignKey(User,on_delete= models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse('home')
        return reverse('post-detail', kwargs={'pk': self.pk})