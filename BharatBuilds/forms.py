from django import forms 

##form creation using django
class registrationforms(forms.Form):
    fullname=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput) 
    # age=forms.IntegerField()
    # password=forms.CharField() 
     

