from django.contrib.auth.models import AbstractUser
from django.db import models

class UserTypes(models.TextChoices):
    EMPLOYER = 'employer', 'Employer'
    MANAGER = 'manager', 'Manager'
    INTERN = 'intern', 'Intern'
    


class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=UserTypes.choices, default=UserTypes.INTERN)

    def __str__(self):
        return self.username
    
    

