from __future__ import unicode_literals
from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.


class Userv1_0(models.Model):
    Uid=models.AutoField(primary_key=True)
    EmailId = models.EmailField(blank=True, null=True)
    Phone=models.CharField(max_length=50,blank=True,null=True)
    Name=models.CharField(max_length=50,blank=True,null=True)
    StateId = models.ForeignKey('collegeData.StateV1_0', blank=True, null = True)
    Password=models.CharField(max_length=255, blank=False, null=False)
    CollegeId=models.ForeignKey('collegeData.CollegeV1_0', blank=True, null = True)
    RegisterTime=models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    def __unicode__(self):
        return unicode(self.EmailId)


