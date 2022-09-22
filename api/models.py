from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(blank=True, null=True, max_length=200)
    body = models.TextField(blank=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.title
    