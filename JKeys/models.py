from datetime import timezone
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django import forms


# Class for ID model
class Id(models.Model):
    # Attributes in database to put in Text Fields
    # Char Fields for all attributes in this part with default='' and maxlength of 200 chars
    name = models.CharField(max_length=200, default="")
    mail = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="")  # TO ENCRYPT
    link = models.CharField(max_length=200, default="")

    # Fields for Creation and Modification Dates
    # Created -> editable=false to do not modify this date
    # Modified -> auto_now=true to be changed automatically
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(auto_now=True)

    # Save function to save Creation and Modification Date
    def save(self, *args, **kwargs):
        ''' On save, update modification date and creation date '''
        # If the element is not yet created -> change creation date to now
        # In every situation, when saved, change modification date to now
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        # Override and give to model new arguments
        return super(Id, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


