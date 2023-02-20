from datetime import timezone
from django.contrib.auth.models import User
from django.db import models
from django import forms


"""
class Profile(models.Model):
    name = models.CharField(max_length=200)
"""

class Id(models.Model):

    name = models.CharField(max_length=200, default="")
    mail = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="")  # TO ENCRYPT
    link = models.CharField(max_length=200, default="")

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)


class CreditCard(models.Model):

    name = models.CharField(max_length=200, default="")
    card_number = models.CharField(max_length=200, default="")  # TO ENCRYPT

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)


class IdCard(models.Model):

    name = models.CharField(max_length=200, default="")
    models.CharField(max_length=200, default="")  # TO ENCRYPT
    first_name = models.CharField(max_length=200, default="")
    middle_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")

    address1 = models.CharField(max_length=200, default="")
    address2 = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    state = models.CharField(max_length=200, default="")
    postal_code = models.CharField(max_length=200, default="")
    country = models.CharField(max_length=200, default="")

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)
