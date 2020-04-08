"""Admin configuration for models"""
from django.contrib import admin

from .models import Question, Choice

#admin.site.register(Question)
#admin.site.register(Choice)

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    """
    Change Choices directly from Questions
    """
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """
    QuestionAdmin design the look of fields in admin section
    """
    #fields = ['pub_date', 'question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes': ['collapse']}),
    ]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
