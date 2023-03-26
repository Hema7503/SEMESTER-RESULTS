'''from django import forms
from .models import Attende
class AttendeForm(forms.ModelForm):
	class Meta:
	  model = Attende
	  fields = '__all__'
	  exclude = ['date', 'time']'''
	  
'''from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'
		exclude = ['M3' , 'DMS' , 'DBMS' , 'CO' , 'OOP' , 'DBMSLAB' , 'OOPLAB' , 'RLAB' , 'WADFSLAB' , 'SGPA' , 'date' , 'time']
		#exclude = ['date' , 'time']	'''  
		
'''from django import forms
from .models import Attende
class AttendeForm(forms.ModelForm):
	class Meta:
		model = Attende
		fields = '__all__'
		#exclude = ['M3' , 'DMS' , 'DBMS' , 'CO' , 'OOP' , 'DBMSLAB' , 'OOPLAB' , 'RLAB' , 'WADFSLAB' , 'SGPA' , 'date' , 'time']
		exclude = ['date' , 'time']'''	 
