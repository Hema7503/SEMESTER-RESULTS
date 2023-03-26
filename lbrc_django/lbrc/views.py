'''from django.shortcuts import render

from .forms import AttendeForm
from .models import Attende
#import pytz

# Create your views here.
def index(request):
  form = AttendeForm()
  #IST = pytz.timezone('Asia/Kolkata')
  #now = datetime.datetime.now(IST)
  
  if request.method == 'POST':
    form = AttendeForm(request.POST)
    if form.is_valid():
      print(form)
      form.save()
    #f = form.save(commit=False)
#f.date = now.strftime('%Y-%m-%d')
#f.time = now.strf('%H:%M:%S.%f')
  context = {'form': form}
  return render(request,'index.html',context) 
   
def get_details(request):
	data = Attende.objects.all()
	context = {'data': data}
	return render(request,'details.html',context)'''
	
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from .forms import AttendeForm
from .models import Student
#from .forms import StudentForm
#from django.shortcuts import render

def webpage1(request):
	return render(request,'result1.html')
def webpage2(request):
	return render(request,'result2.html')	
def webpage3(request):
	return render(request,'result3.html')
#def webpage4(request):
#	return render(request,'results4.html')

def index(request):	
	return render(request,'index.html')
def result(request):
	if request.method == 'POST':
		#is_private = request.POST['is_private']
		RedgNo = request.POST.get('RedgNo')
		#RedgNo = str(request.POST.get('RedgNo'))
		#student = Student.objects.get(RedgNo=RedgNo)
		student = Student.objects.get(RedgNo=RedgNo)
		#RedgNo = student.RedgNo
		M3 = student.M3
		DMS = student.DMS
		DBMS = student.DBMS
		CO = student.CO
		OOP = student.OOP
		DBMSLAB = student.DBMSLAB
		OOPLAB = student.OOPLAB
		RLAB = student.RLAB
		WADFSLAB = student.WADFSLAB
		SGPA = student.SGPA
		
		params = {
			'RedgNo' : RedgNo,
			'M3' : M3,
			'DMS' : DMS,
			'DBMS' : DBMS,
			'CO' : CO,
			'OOP' : OOP,
			'DBMSLAB' : DBMSLAB,
			'OOPLAB' : OOPLAB,
			'RLAB' : RLAB,
			'WADFSLAB' : WADFSLAB,
			'SGPA' : SGPA
		}
		return render(request, 'result.html',params)
	else:
		print('get method')
		return render(request, 'result.html')		
		
def admin_login(request):
	if 'user' in request.session:
		return render(request,'admin_panel.html')
	else:
		return render(request, 'admin-login.html')
		
def admin_panel(request):
	if 'user' in request.session:
		students = Student.objects.all()
		params = {'students': students}
		return render(request, 'admin_panel.html',params)
	else:
		if request.method == 'POST':
			user_name = request.POST['uname']
			pass_word = request.POST['pwd']
			if user_name == 'Toffee' and pass_word == 'Shinchan@panda':
				request.session['user'] = user_name
				students = Student.objects.all()
				params = {'students': students}
				return render(request,'admin_panel.html',params)
			else:
				return render(request, 'admin-login.html')
		else:
			return render(request,'admin-login.html')
			
def delete_student(request, id):
	get_stu = Student.objects.get(id=id)
	get_stu.delete()
	return redirect('/admin_panel')
	
def edit_student(request, id):
	get_stu = Student.objects.get(id=id)
	params = {'student' : get_stu}
	return render(request, 'edit.html',params)
	
def edit_confirm(request, id):
	if request.method == 'POST':
		get_stu = Student.objects.get(id=id)
		get_stu.RedgNo = request.POST['RedgNo']
		get_stu.M3 = request.POST['M3']
		get_stu.DMS = request.POST['DMS']
		get_stu.DBMS = request.POST['DBMS']
		get_stu.CO = request.POST['CO']
		get_stu.OOP = request.POST['OOP']	
		get_stu.DBMSLAB = request.POST['DBMSLAB']
		get_stu.OOPLAB = request.POST['OOPLAB']		
		get_stu.RLAB = request.POST['RLAB']
		get_stu.WADFSLAB = request.POST['WADFSLAB']
		get_stu.SGPA = request.POST['SGPA']	
		get_stu.save()
		return redirect('/admin_panel')
	else:
		return redirect('/admin_login')
		
def admin_logout(request):
	del request.session['user']
	return redirect('/')				
			
def add_student(request):
	return render(request, 'add_student.html')
	
def add_confirm(request):
	if request.method == 'POST':
		RedgNo = request.POST['RedgNo']
		M3 = str(request.POST['M3'])
		DMS = str(request.POST['DMS'])
		DBMS = str(request.POST['DBMS'])
		CO = str(request.POST['CO'])
		OOP = str(request.POST['OOP'])	
		DBMSLAB = str(request.POST['DBMSLAB'])
		OOPLAB = str(request.POST['OOPLAB'])		
		RLAB = str(request.POST['RLAB'])
		WADFSLAB = str(request.POST['WADFSLAB'])
		SGPA = float(request.POST['SGPA'])
		add_student =   Student.objects.create(RedgNo=RedgNo,M3=M3,DMS=DMS,DBMS=DBMS,
		                CO=CO,OOP=OOP,DBMSLAB=DBMSLAB,OOPLAB=OOPLAB,RLAB=RLAB,
		                WADFSLAB=WADFSLAB,SGPA=SGPA)
		add_student.save()
		return redirect('/admin_panel')
	else:
		return redirect('/admin_panel') 	
		
'''def Index(request):
	form = AttendeForm()
	if request.method == 'POST':
		form = AttendeForm(request.POST)
		if form.is_valid():
			print(form)
			form.save()
	context = {'form' : form}
	return render(request,'Index.html',context)
	
def get_details(request):
	data = Attende.objects.all()
	context = {'data': data}
	return render(request,'details.html',context)		
	
def match(request):
	if request.method == 'POST':
		RedgNo = request.POST['RedgNo']
		if RedgNo == Student.RedgNo:
			request.session['RedgNo']=RedgNo
			students = Student.objects.all()
			params={'students' : students}
			return render(request,'result.html',params)
		else:
			return render(request, 'index.html')'''
			
					
			
	
					
					
									

		
	
	

  
