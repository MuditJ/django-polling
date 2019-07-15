from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

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
	#return HttpResponse(f"You're looking at question {question_id}:")
	#Make DB call to fetch the question with given id
	
	try:
		question = Question.objects.get(id = question_id)		
	except Question.DoesNotExist:
		raise Http404("Question doesnt exist")
	else:
		#return HttpResponse(f"You're looking at question {question_id}: {question.question_text}")
		return render(request,'polls/detail.html',{'question' : question})
	#A shortcut for this routine of "Fetch an object from DB and return it or return a 404 if object doesnt exist"
	#is to use the get_object_or_404 function


def results(request,question_id):
	#return HttpResponse(f"Results of the question {question_id}")
	question = get_object_or_404(Question,pk = question_id)
	return render(request,'polls/results.html',{'question' : question})

def vote(request,question_id): #A POST request comes in to the corresponding route
	#return HttpResponse(f"Voting on the question {question_id}")
	question = get_object_or_404(Question,pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		#Redisplay the question voting form
		return render(request,'polls/detail.html',{'question':question,
			'error_message':'You didnt select a choice'})
	else:
		selected_choice.votes += 1
		selected_choice.save() #Update the value in DB
		return HttpResponseRedirect(reverse('polls:resultwa',args=(question.id,)))
