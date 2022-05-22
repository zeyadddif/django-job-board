from tkinter import CASCADE
from django.db import models

# Create your models here.
JOB_TYPE = (
    ('FullTime', 'FullTime'),
    ('PartTime', 'PartTime'),
)


class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100, choices=JOB_TYPE)
    des = models.TextField(max_length=1000)
    publishedon = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
