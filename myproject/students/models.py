from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.IntegerField(unique=True)
    department = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.name