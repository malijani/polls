""" Polls app models """
from django.db import models

class Question(models.Model):
    """ Question model """
    # id (pk) will generate automatically + auto increament + unique
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """ Printing object will return question_text : pub_date """
        #return f'{self.question_text} : {self.pub_date}\n'
        return self.question_text

class Choice(models.Model):
    """ Choice model (Each Question will have multiple Choices) """
    # id (pk) will generate automatically + auto increament + unique
    # ForeignKey to Question model will relate the Choice to Question
    # The relation type in here is one(Question) to many(Choices)
    question_field = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """ Printing object will return choice_text : votes """
        #return f'{self.choice_text} : {self.votes}'
        return self.choice_text
