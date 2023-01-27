from django.db import models
# Create your models here.

class Testing(models.Model):
    name = models.TextField(max_length=199)
    password = models.TextField(max_length=199)


class gateway(models.Model):
#     # user = models.TextField(max_length=199)
    name = models.TextField(max_length=199)
    city = models.TextField(max_length=199)
    # org_id = models.TextField(max_length=199)
    # latitude = models.TextField(max_length=199)
    # longitude = models.TextField(max_length=199)
    # loc_name = models.TextField(max_length=199)
    # loc_region = models.TextField(max_length=199)

class gateway_details(models.Model):
    user = models.TextField(max_length=199)
    servername = models.TextField(max_length=199)
    gateway_name = models.TextField(max_length=199)
    org_id = models.TextField(max_length=199)
    latitude = models.TextField(max_length=199)
    longitude = models.TextField(max_length=199)
    loc_name = models.TextField(max_length=199)
    loc_region = models.TextField(max_length=199)

