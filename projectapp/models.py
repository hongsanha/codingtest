from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    number=models.TextField()
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Blog,on_dellete=models.CASCADE)