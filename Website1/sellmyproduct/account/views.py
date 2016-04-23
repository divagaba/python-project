from django.shortcuts import render 
from django.http import HttpResponse,HttpResponseRedirect
from .forms import registerForm ,loginform, contactusform, changePassForm, forgetform,recoverypwdform,addprodform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as auth_login,logout as auth_logout
from account.models import Contactus , Forgetpass,Addprod

from django.http import Http404
import uuid


from django.contrib.auth.decorators import login_required


def index(request):
	print "Iam in index"
	return render(request,'index.html')

def loginSub(request):
	if request.method == 'POST':
		form = loginform(request.POST)
		if form.is_valid():
			myusr  = form.cleaned_data['username']
			mypass =  form.cleaned_data['password']
			user = authenticate(username=myusr, password=mypass)
			if user is not None:
				if user.is_active:
					print "User is valid, active and authenticated" 
					auth_login(request,user)
					return HttpResponseRedirect("/")
				else:
					print "The password is valid, but the account has been disabled!"
			else:
				print "The username and password were incorrect."

			return render(request,'login.html',{'form':form,'msg':'you can sucessfully loggin'})
		else:
			return render(request,'login.html', {'form':form})
	else:
		return HttpResponse("permission denied")

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect("/")

@login_required
def myhome(request):
	return render(request,'home.html')

@login_required
def changepass(request):
	form  = changePassForm()
	return render(request,'setpass.html',{'form':form})


@login_required
def changepasssubmit(request):
	if request.method == 'POST':
		form = changePassForm(request.POST)
		if form.is_valid():
			oldpass = form.cleaned_data['oldPass']
			newpass = form.cleaned_data['newPass']
			currentUser = str(request.user.username)
			user = authenticate(username=currentUser,password=oldpass)
			if user is not None:
				user.set_password(newpass)
				user.save()
				return render(request,'setpass.html',{'form':form,'msg':'Password Changed Success !'})
			else:
				return render(request,'setpass.html',{'form':form,'msg':'Old Password mismatch!'})
		else:
			return render(request,'setpass.html',{'form':form})
	else:
		return HttpResponseRedirect('/')



def loginme(request):
	form = loginform()
	return render(request,'login.html',{'form':form})

def contactsub(request):
	if request.method == 'POST':
		form = contactusform(request.POST)
		if form.is_valid():
			cont = Contactus(name=form.cleaned_data['name'])
			cont.email = form.cleaned_data['email']
			cont.Query = form.cleaned_data['Query']
			cont.save()
			return render(request,'contactme.html',{'form':form,'msg':'Thank you For Contacting us !'})
		else:
			return render(request,'contactme.html',{'form':form})
	else:
		form = contactusform()
		return render(request,'contactme.html',{'form':form})


def registerSub(request):
	if request.method == 'POST':
		form = registerForm(request.POST)
		if form.is_valid():
			username 	= form.cleaned_data['username']
			email		= form.cleaned_data['email']
			first_name  = form.cleaned_data['first_name']
			last_name   = form.cleaned_data['last_name']
			password  	= form.cleaned_data['password']

			user = User.objects.create_user(username=username,password=password)
			user.email = email
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			return render(request,'register.html',{'msg':'User Registered Success !'})
		else:
			return render(request,'register.html',{'form':form})
	else:
		return HttpResponse("Access Forbidden")


def registerme(request):
	form = registerForm()
	return render(request,'register.html',{'form':form})


			
			
			
			
			
	
	

		

def forgetpass(request):
	if request.method=='POST':
		form=forgetform(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			try:uu = User.objects.get(username=username)
			except:uu = None
			if uu is None:
				return render(request,'forgetpwd.html',{'form':form,'message':'User Not Found!!!'})
			else:
				try:
					forgetInsta = Forgetpass.objects.filter(user=uu.id)
					forgetInsta.delete()
				except:pass

				randomid = uuid.uuid4()

				pre_domain =  str(request.META['HTTP_HOST'])
				makeUrl = "http://%s/home/recover/%s/"%(pre_domain,randomid)
				print makeUrl
				mailBody = """ 
					Hi , 
					Please Click on Following link to reset your Password 

					%s

					Thanks

				"""%(makeUrl)


				forget = Forgetpass(token=randomid,user=uu)
				forget.save()
			return render(request,'forgetpwd.html',{'form':form,'msg':'We have sent mail to reset your password!!'})
		else:
			return render(request,'forgetpwd.html',{'form':form})
	else :
		form  = forgetform()
		return render(request,'forgetpwd.html',{'form':form})

def recoverpass(request,token):
	token = str(token)
	token = token.split("/")[0]

	if request.method == 'POST':
		form = recoverypwdform(request.POST)
		if form.is_valid():
			password = form.cleaned_data['newpass']
			newpass = form.cleaned_data['confirmpass']
			if password == newpass:
				try:
					stat = Forgetpass.objects.get(token=token)
					tokenStat = True
				except:pass
				userid = int(stat.user.id)

				user = User.objects.get(pk=userid)
				user.set_password(newpass)
				user.save()
				stat.delete()

				return render(request,'pwd.html',{'form':form})
			else :
		
				return render(request,'recovery.html',{'form':form,'token':token,'msg':"Password Mismatch!!!!!"})
		else :
			 return HttpResponse("Access Denied!!")
	else:
		tokenStat = False
		try:
			stat = Forgetpass.objects.get(token=token)
			tokenStat = True
		except:pass

		if tokenStat == False:
			
			return Http404("Page not Found")
		else:
			userID = stat.user.id

		form  = recoverypwdform()
		return render(request,'recovery.html',{'form':form,'userid':userID,'token':token})

def freqaskd(request):
	return render(request,'faq.html')
def privacy(request):
	return render(request,'privacy.html')
def terms(request):
	return render(request,'terms.html')

@login_required	
def add(request):
	form=addprodform()
	return render(request,'post.html',{'form':form})