from django.db import models

# Create your models here.

class Olympics(models.Model):
    country_name = models.CharField(max_length=30)
    medals_won = models.CharField(max_length=30)

    def __str__(self):
        return self.country_name