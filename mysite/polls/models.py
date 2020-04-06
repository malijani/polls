"""Models for polls application"""
import datetime
from django.db import models
from django.utils import timezone


#THE DATABASE MODEL IS : ONE TO MANY
class Question(models.Model):
    """
    Question class is the main model
    which has a QUESTION TEXT and a PUBLISH DATE
    and each Question is related to a Choice
    """
    # The id of each Question is its pk and Choice uses it as ForeignKey
    # The primary key generates automatically!
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        """
        was_published_recently() returns the questions that
        published in 1 days before now!
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    """
    Choice class is the child model for Question
    which has a CHOICE TEXT and VOTE TALLY related
    to a Question field.
    """
    # Using each Question pk as a foreign key
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
