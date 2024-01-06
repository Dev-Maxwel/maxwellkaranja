from django.db import models

class emailingInfo(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=70, blank=True, null=True)
    message = models.TextField(max_length=10000, blank=True, null=True)
    