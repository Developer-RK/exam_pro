from django.db import models

# Create your models here.
class MessageTemplates(models.Model):
  template = models.TextField()
  
  def  __str__(self) -> str:
    return self.template
