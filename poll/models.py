from django.db import models


class PollModel(models.Model):
    question = models.TextField()
    optionOne = models.CharField(max_length=30)
    optionTwo = models.CharField(max_length=30)
    optionThree =models.CharField(max_length=30)
    optionOneCount = models.IntegerField(default=0)
    optionTwoCount = models.IntegerField(default=0)
    optionThreeCount  = models.IntegerField(default=0)

    def __str__(self):
        return self.question

    def Total(self):
        total =self.optionOneCount + self.optionThreeCount + self.optionTwoCount
        return total
