from django import forms
from django.forms import ModelForm


from django.contrib.auth.models import User


# class registerForm(forms.Form):
# 	first_name = forms.CharField(label="Enter First Name", max_length=100)
# 	last_name = forms.CharField(label="Enter Last Name",max_length=200)
# 	username = forms.CharField(label="Enter Username",max_length=200)
# 	email = forms.EmailField(label="Enter your Email",max_length=200)



class registerForm(ModelForm):
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email = forms.CharField(required=True)
	class Meta:
		model = User
		fields = ('email','username','first_name','last_name','password')


class loginform(forms.Form):
	username=forms.CharField(required=True)
	password=forms.CharField(required=True)



class changePassForm(forms.Form):
	oldPass 	= forms.CharField(max_length=200,required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Old Password'}))
	newPass		= forms.CharField(max_length=200,required=True,widget=forms.TextInput(attrs={'placeholder':'Enter New Pasword'}))

class contactusform(forms.Form):
	name = forms.CharField(max_length=200,required=True,widget=forms.TextInput(attrs={'placeholder':'Enter your Name'}))
	email = forms.CharField(max_length=200,required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Your email'}))
	Query=forms.CharField(max_length=200,required=True,widget=forms.TextInput(attrs={'placeholder':'Enter your Query'}))

class forgetform(forms.Form):
	 username=forms.CharField(max_length=200,required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Your Username'}))

class recoverypwdform(forms.Form):
	newpass =	 forms.CharField(max_length=200,required=True,widget=forms.TextInput(attrs={'placeholder':'Enter New Pasword'}))
	confirmpass = forms.CharField(max_length=200,required=True,widget=forms.TextInput(attrs={'placeholder':'Enter New Pasword'}))

class addprodform(forms.Form):
	category=forms.CharField(max_length=200,required=True)
	title=forms.CharField(max_length=200,required=True)
	desc=forms.CharField(max_length=200,required=True)
	name=forms.CharField(max_length=200,required=True)
	email=forms.CharField(max_length=200,required=True)
	
