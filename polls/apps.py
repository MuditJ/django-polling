from django.apps import AppConfig

#This class needs to be 'registered' i.e. added in the
#INSTALLED_APPS list
class PollsConfig(AppConfig):
    name = 'polls'
