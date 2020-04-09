""" Views of polls app which renders output """
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from .models import Question, Choice

def index(request):
    """ Get questions and display them """
    # list 5 latest questions
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # configure frontend
    template = 'polls/index.html'
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, template, context)

def detail(request, question_id):
    """ Show details of a specific Question and Choices"""
    # try to get question by id if doesn't exist will show http404
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # configure frontend
    template = 'polls/detail.html'
    context = {
        'question': question,
    }
    return render(request, template, context)

def result(request, question_id):
    """ Get Question and display results """
    # get question by id or show http404
    question = get_object_or_404(Question, pk=question_id)
    # configure frontend
    template = 'polls/result.html'
    context = {
        'question': question,
    }
    return render(request, template, context)

def vote(request, question_id):
    """ Vote for a question choice """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay Question voting form
        return render(
            request,
            'polls/detail.html',
            {
                'question': question,
                'error_message': "You didn't select a choice",
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a user
        # hits the back button
        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))
