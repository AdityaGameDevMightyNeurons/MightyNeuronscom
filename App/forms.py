from cProfile import label
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Conctact

class ContatcForm(ModelForm):
    class Meta:
        model= Conctact
        fields = ['Name', 'Email', 'Phone', 'Meeseges']
        labels = {
            'Name': "Your Name",
            'Email':"Your Email", 
            'Phone':"Your Phone Number", 
            'Meeseges':"Your Messege"
        }
        widgets = {
            'Name': forms.TextInput(attrs={"class":"form-input" ,"id":"contact-email-2","placeholder":"Your Name", "type":"text", "name":"name" ,"data-constraints":"@Required"}),
            'Email': forms.EmailInput(attrs={"class":"form-input" ,"id":"contact-email-2", "type":"email","placeholder":"E-mail", "name":"Email" ,"data-constraints":"@Required"}),
            'Phone': forms.TextInput(attrs={"class":"form-input" ,"id":"contact-phone-2", "name":"Phone" ,"placeholder":"Phone eg:+91 9999999999","data-constraints":"@Required"}),
            'Meeseges': forms.Textarea(attrs={"class":"form-input" ,"id":"contact-message-2", "type":"text","placeholder":"Messege", "name":"Messeges" ,"data-constraints":"@Required"}),
        }

