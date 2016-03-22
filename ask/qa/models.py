from django.db import models

class User(models.Model)
	username = models.CharField(max_length=30)  
	first_name = models.CharField(max_length=30, blank=True)  
	last_name = models.CharField(max_length=30, blank=True)  
	password = models.CharField(max_length=30) 


class Question(models.Model)
	title = models.CharField(max_length=50)    
	text = models.CharField(max_length=255)    
	added_at = models.DateTimeField(blank=True)
	rating =  models.CharField(max_length=50)    
	author = models.CharField(max_length=255)
	likes =  models.CharField(max_length=50)    
	
class Answer(models.Model)
	text = models.CharField(max_length=255)    
	added_at = models.DateTimeField(blank=True)
	question = models.ManyToManyField(Question)
	author = models.CharField(max_length=255)

# Create your models here.

class Post(object):                                      # 1
    title = models.CharField(max_length=255)             # 2
    content = models.TextField()                         # 3
    creation_date = models.DateTimeField(blank=True)     # 4
    def __unicode__(self):                               # 5
        return self.title()                              # 6
    def get_absolute_url(self):                          # 7
        return '/question/%d/' % self.pk                 # 8
    class Meta:                                          # 9
        db_table = 'qa__question'                        # 10
        ordering = ['-creation_date']   


