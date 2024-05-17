from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Items(TimeStampedModel):
    name = models.CharField(max_length=20)
    price = models.FloatField(max_length=20)
    slug = models.SlugField(unique=True, max_length=30)
    image = models.ImageField(upload_to='items/')

    def str(self):
        return self.name
