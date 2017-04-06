from __future__ import unicode_literals

from django.db import models

# Create your models here.


class StateV1_0(models.Model): #model for state
    StateId = models.AutoField(primary_key=True)
    StateName = models.CharField(max_length=200, blank=False, null=False)
    def __unicode__(self):
        return str(self.StateName)

class CollegeV1_0(models.Model): #model for college
    CollegeId = models.AutoField(primary_key=True)
    College = models.CharField(max_length=200, blank=False, null=False)
    StateId = models.ForeignKey('StateV1_0', blank=True, null = True)
    def __unicode__(self):
        return str(self.College)