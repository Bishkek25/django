from tkinter.constants import CASCADE

from django.db import models

'''
posts = Posts.objects.all() SELECT * FROM posts
posts = Posts.objects.get(id=1) SELECT DISTINCT FROM POSTS WHERE id=1
posts = Posts.objects.filter(name="a")
posts = Posts.objects.create(title="a", description="b", rate=3)
'''

class Category(models.Model):
    title = models.CharField(max_length=56)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=56)

    def __str__(self):
        return self.title

class Post(models.Model):
    catergory = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True,blank=True)
    title = models.CharField(max_length=56)
    description = models.CharField(max_length=256)
    rate = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    image = models.ImageField(null=True, blank=True)

def __str__(self):
        return f"{self.title}: {self.description}"

