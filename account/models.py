from django.db import models

class CustomUser(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # storing in plain text (not secure)

    def __str__(self):
        return self.email
