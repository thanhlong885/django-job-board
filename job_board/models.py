from django.db import models

# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} at {self.company} | ${self.salary}"
    
    
class Application(models.Model):
    job = models.ForeignKey("JobPosting", on_delete=models.CASCADE, related_name="applications")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    resume = models.FileField(upload_to="resumes/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Application by {self.name} for job {self.job.title}"
    