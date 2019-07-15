from django.db import models

# Create your models here.
#2 models - Question(has question text and publication date)
# and Choice(option text and vote tally)

#Each Choice is associated with a Question

#EAch model has a number of class variables that represent a database field in the model
class Question(models.Model): #A model class must inherit from Django's Model superclass
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete = models.CASCADE)
	#On Deleting a question, delete all the corresponding choices as well
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)

	def __str__(self):
		return self.choice_text

#The two models have a many-to-one relationship: many Choice model class
#instances map to a single Question class instance(but not the other way aroung)


#Using the models defined here, Django creates a database schema for the
#application, creates a table for each model and allows the user to 
#manipulate the actual persistent data via the ORM. 


#Migrations are python files stored in the project which record what
#changes are to be made to the database schema. THis can include
#adding new fields, removing fields/constraints while developing the project
#make migrations command creates the migrations for the latest changes
#migrate command executes these changes.