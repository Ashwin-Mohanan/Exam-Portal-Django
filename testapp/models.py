from tkinter import HIDDEN
from django.db import models
# Create your models here.

class Q(models.Model):
    Qta1=models.CharField(max_length=50,default='SOME STRING')
    op1=models.CharField(max_length=20,default='')
    op2=models.CharField(max_length=20,default='')
    op3=models.CharField(max_length=20,default='')
    op4=models.CharField(max_length=20,default='')
    correctop=models.CharField(max_length=100,default='')
    
    
class Java(models.Model):
    Qta1=models.CharField(max_length=500,default='SOME STRING')
    op1=models.CharField(max_length=200,default='')
    op2=models.CharField(max_length=200,default='')
    op3=models.CharField(max_length=200,default='')
    op4=models.CharField(max_length=200,default='')
    correctop=models.CharField(max_length=1000,default='')
    