from django.shortcuts import render
from .models import *
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request ,'index.html')

def contact(request):
    if request.method == "POST":
        try:
            if request.POST["name"] == "" or request.POST["email"] == "" or request.POST["subject"] == "" or request.POST["msg"] == "":
                context ={
                    "msg_d" : "All Field mandatory....."
                }
                return render(request,'contact.html',context=context)
            else:
                contact = Contact.objects.create(
                    name = request.POST["name"],
                    email =  request.POST["email"],
                    subject = request.POST["subject"],
                    msg = request.POST["msg"],
                )
                contact.save()
                subject = contact.subject
                message = f"name : {contact.name} " + "\n" + f'email : {contact.email}' + "\n" + f"subject : {contact.subject}" + "\n" + f"message : {contact.msg}" 
                email_from = contact.email
                recipient_list = [ settings.EMAIL_HOST_USER, ]
                send_mail( subject, message, email_from, recipient_list )

                context ={
                    "msg_s" : "successfull ....."
                }
                return render(request,'contact.html',context=context)
        except:
            context ={
                    "msg_d" : "something went wrong"
                }
            return render(request,'contact.html',context=context)
    else:
        return render(request ,'contact.html')