from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Choice, Question
# Create your views here.

def index(request):
	#print(type(request))
	#return HttpResponse("Hello World. This is the index page of the polling app.")
	latest_questions = Question.objects.order_by('-pub_date')[:5]
	output = '\n '.join([q.question_text for q in latest_questions])
	#return HttpResponse(output)
	template = loader.get_template('polls/index.html')
	context = {'latest_questions' : latest_questions} #Data to be passed to template. Generally put in a 'context' dictionary
	return HttpResponse(template.render(context,request))


#Instead of directly returning an HTTP response from a view function,
#the data to be returned can be passed to a template which renders that
#data ro return a customized page.


#4 views in the polling app:
#An index page to display the latest questions, A detail page
#that shows a question with a form to vote
#Results page to display results for a question
#Vote action: Handles voting for a particular choice in a particular question

#The views need to be registered to a route in the URLConf (app level urls.py)

def detail(request,question_id):
	return HttpResponse(f"You're looking at question {question_id}")

def results(request,question_id):
	return HttpResponse(f"Results of the question {question_id}")

def vote(request,question_id):
	return HttpResponse(f"Voting on the question {question_id}")
