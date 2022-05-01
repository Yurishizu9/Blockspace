from django.db import models

# Create your models here.


class User(models.Model):
    '''metamask wallet addresses are 42 characters long but in future
    I will support other wallet address whcih may have more or less characters in them
    wallet address will be the foreign key '''
    wallet_address = models.CharField(max_length=42, unique=True, null=True, blank=True)
    username = models.CharField(max_length=16, editable=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    # method allows to print instances of the model when needed
    # a string representation of the model

    def __str__(self):
        return self.username
