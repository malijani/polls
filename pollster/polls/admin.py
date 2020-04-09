""" Register polls models into admin area """
from django.contrib import admin

from .models import Question, Choice

# Change Admin Site Header
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster admin area"

# Register models
# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    """ ChoiceInline is a TabularInline that will show Choices in Question section """
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    """ Configurations of main QuestionAdmin model """
    # fieldsets tuple : question_text , pub_date
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # configure inlines
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
