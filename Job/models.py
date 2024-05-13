from django.db import models
from myapp.models import User



class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id = models.AutoField(primary_key=True)  # Auto-incrementing job ID
    title = models.CharField(max_length=100)
    salary = models.CharField(max_length=5)
    experience = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    skills = models.TextField()  # Skills required for the job
    requirements = models.TextField()  # Job requirements
    responsibilities = models.TextField()  # Job responsibilities
    qualifications = models.TextField()  # Required qualifications
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)


