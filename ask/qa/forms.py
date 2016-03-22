from django import forms

class AskForm(forms.Form)
	title = forms.CharField(max_len=100)
	text = forms.CharField(widget=forms.Textarea)
	
class AnswerForm(forms.Form)
	text = forms.CharField(widget=forms.Textarea)
	question = 

def __init__(self, *args, **kwargs):
	super(AddPostForm, self).__init__(*args, **kwargs)	
	
	
def clean(self)

	
	

def save(self):                                                         
                question = Question.objects.create()                            
                print self.cleaned_data, 'in save'                              
                print ''                                                        
                #cd = self.cleaned_data                                         
                #question.title = cd['title']                                   
                #question.text = cd['text']                                     
                #question.author = "Roman"                                      
                #question.save()                                                
                return question  