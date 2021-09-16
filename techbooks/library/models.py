from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    num_pages = models.IntegerField(default=0)
    publish_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=8)
    color = models.CharField(max_length=32, blank=True, null=True)
    isbn13 = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.title
