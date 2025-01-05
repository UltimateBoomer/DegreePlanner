from django.db import models
from django.utils.translation import gettext_lazy as _

class Season(models.TextChoices):
    FALL = 'F', _('Fall')
    WINTER = 'W', _('Winter')
    SPRING = 'S', _('Spring')

class Term(models.Model):
    code = models.IntegerField()
    year = models.IntegerField()
    season = models.CharField(max_length=1, choices=Season.choices)

class Subject(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Course(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    subject = models.CharField(max_length=100)
    number = models.IntegerField()
    description = models.CharField(max_length=1000)

class PreReq(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='%(class)s_requests_created')
    prereqOrGroup = models.ManyToManyField(Course)

class CoReq(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='%(class)s_requests_created')
    coreqOrGroup = models.ForeignKey(Course, on_delete=models.CASCADE)

class AntiReq(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='%(class)s_requests_created')
    antireq = models.ForeignKey(Course, on_delete=models.CASCADE)

class Degree(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
