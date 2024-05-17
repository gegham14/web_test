from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=35)
    review = models.TextField(max_length=350)
    model_text = models.CharField(max_length=40,blank=True)

    def __str__(self):
        return self.full_name


