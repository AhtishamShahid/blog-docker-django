"""
Models are created here
"""
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """
    Question Model
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        String representation of class
        """
        return self.question_text

    def was_published_recently(self):
        """
        To test if is recently published
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    """
    Choice Model
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        String representation of class
        """
        return self.choice_text

# class ChoiceInline(admin.TabularInline):
#     model = Question

# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [
#         ChoiceInline,
#     ]
