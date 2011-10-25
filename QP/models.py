from django.db import models
from django.utils.safestring import mark_safe 
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.conf import settings
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length = 200)
    added_at = models.DateTimeField(auto_now=True)
    description = models.TextField( null = True , blank = True)
    
    def __unicode__(self):
        return self.name

class Subject(models.Model):
    subject_code = models.CharField(max_length = 200 , null = True , blank = True)
    name = models.CharField(max_length = 200)
    department = models.ForeignKey('Department')
    added_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null = True , blank = True)
    
    def __unicode__(self):
        return self.name

class Question(models.Model):
    subject = models.ForeignKey('Subject')
    question = models.TextField()
    question_types = (
        ('A' , 'Part A'),
        ('B' , 'Part B'),
        )
    question_type = models.CharField(max_length = 20 , choices = question_types)
    unit_number = models.PositiveSmallIntegerField(null = True , blank = True)
    comments = models.TextField( null = True , blank = True)
    added_at = models.DateTimeField(auto_now=True)
    
    def display_question(self): 
        return mark_safe(self.question)
    
    def __unicode__(self):
        return self.display_question()
class ExamConfiguration(models.Model):
    exam_name = models.CharField(null = False , blank =False , max_length = 30)
    num_of_questions_in_partA = models.IntegerField(null = False , blank = False)
    num_of_questions_in_partB = models.IntegerField(null = False , blank = False)
    unit1 = models.BooleanField()
    unit2 = models.BooleanField()
    unit3 = models.BooleanField()
    unit4 = models.BooleanField()
    unit5 = models.BooleanField()
    
    def getUnitList(self):
        unitList =[]
        if(self.unit1):
            unitList.append(1)
        if(self.unit2):
            unitList.append(2)
        if(self.unit3):
            unitList.append(3)
        if(self.unit4):
            unitList.append(4)
        if(self.unit5):
            unitList.append(5)
        
        return unitList
    
    def __unicode__(self):
		return self.exam_name
