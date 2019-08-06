"""Edit and add admin panel modules"""

from django.contrib import admin
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    """To add choice field in admin panel in question editor"""

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """Updated question view for admin"""

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
