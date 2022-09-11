'''App models'''
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    '''Questions table'''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return str(self.question_text)
    def was_published_recently(self):
        '''Is published recently if newer than x days'''
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    '''Choices table'''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return str(self.choice_text)
