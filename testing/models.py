from django.db import models

# Create your models here.
class ApplicationTesting(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    password = models.TextField()
    # print(name,"name")

    class Meta:
        managed = False
        db_table = 'application_testing'

