from django.db import models

# Create your models here.
class SignupModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)

    def __str__(self):
        return self.name