from django.db import models

# Create your models here.
class pythoncode(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    code=models.TextField() 

    def __str__(self):
        return self.name