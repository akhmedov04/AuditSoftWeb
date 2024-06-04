from django.db import models

class Maqola(models.Model):
    title =models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    text = models.TextField()
    photo = models.FileField()
    def __str__(self):
        return self.title