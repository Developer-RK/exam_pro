from django.db import models

# Create your models here.
class TaskMessages(models.Model):
  message = models.TextField()
  date = models.DateField()
  time = models.TimeField()
  
  
  def  __str__(self) -> str:
    return self.message