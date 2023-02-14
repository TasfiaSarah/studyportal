from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

#to remove extra s in notess which is 
#in admin portal
    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"

    def __str__(self):
        return self.title #notes er title ta show korbe

class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)

    class Meta:
        verbose_name = "todo"
        verbose_name_plural = "todo"
    def __str__(self):
        return self.title










