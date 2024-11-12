from django.contrib.auth.models import AbstractUser
from django.db import models

class UserTypes(models.TextChoices):
    EMPLOYER = 'employer', 'Employer'
    MANAGER = 'manager', 'Manager'
    INTERN = 'intern', 'Intern'
    ADMIN = 'admin', 'Admin'
    


class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=UserTypes.choices, default="")
    position = models.CharField(max_length=50, default="", null=True)

    def __str__(self):
        return self.username
    



class PerformanceReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # employee or intern
    date = models.DateTimeField(auto_now_add=True)
    productivity_score = models.IntegerField()
    punctuality_score = models.IntegerField()
    collaboration_score = models.IntegerField()
    goals = models.TextField()
    feedback = models.TextField()

    def __str__(self):
        return f"Review for {self.user.username} on {self.date}"