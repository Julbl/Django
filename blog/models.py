from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from datetime import datetime, date
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    # любой пользователь может быть автором множества записей
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,null=True
    )
    image = models.ImageField(null=True, upload_to='images', blank=True)
    body = models.TextField(null=True)
    post_date = models.DateField(auto_now_add=True, null=True )
    category = models.CharField(max_length=255, default='Cats', null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('post_detail', args=(str(self.id)))
        return reverse('home')
