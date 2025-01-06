from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class UserTypes(models.TextChoices):
    EMPLOYER = 'employer', 'Employer'
    MANAGER = 'manager', 'Manager'
    INTERN = 'intern', 'Intern'
    ADMIN = 'admin', 'Admin'
    


class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=UserTypes.choices, default="")
    position = models.CharField(max_length=100, blank=True, null=True)

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
    
    
#assign Goals
class Goal(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('achieved', 'Achieved'),
        ('missed', 'Missed'),
    ]
    title = models.CharField(max_length=100, null=True)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES)
    progress = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    deadline = models.DateTimeField(null=True)
    assigned_to = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="goals", null=True)
    completed = models.BooleanField(default=False, null=True)

    def check_deadline(self):
        """Check if the goal's deadline is missed and update the status."""
        if self.deadline and now() > self.deadline:
            self.status = 'missed'
            self.save()

    def __str__(self):
        return self.title if self.title else "Untitled Goal"
    

class ReviewScheduling(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=100)
    review_date = models.DateField()
    review_time = models.TimeField()

    def __str__(self):
        return f"{self.review_title} - {self.review_date.strftime('%Y-%m-%d')} at {self.review_time.strftime('%H:%M')}"
