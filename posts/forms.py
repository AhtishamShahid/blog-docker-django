"""
Add forms here
"""
from django.forms import ModelForm
from .models import Comments


class CommentForm(ModelForm):
    """
    Comment form template
    """

    class Meta:
        model = Comments
        fields = ['text']
