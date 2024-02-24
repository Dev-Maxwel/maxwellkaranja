from django.shortcuts import render
from .models import emailingInfo
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from chat import *

def home(request):
    #sending mail
    if request.method == 'POST':
        name = request.POST.get("name").decode('utf-8')
        phone = request.POST.get("phone").decode('utf-8')
        message = request.POST.get("message").decode('utf-8')
        email = request.POST.get("email").decode('utf-8')
        
        #send_mail function parameters
        send_mail(
            f"Message from {name}",
            f"{message}\n\nSender's Name: {name}\nPhone: {phone}\nEmail: {email}",
            email,  #sender's email
            ['developermaxwellkaranja@gmail.com', "mxkaranja@gmail.com"],  #recipient's email
            fail_silently=False,
        )

        # Save the email sending details to the database
        emailInfo = emailingInfo(name=name, phone=phone, email=email, message=message)
        emailInfo.save() 
        return render(request, 'index.html')
    else:
        pass
    return render(request, 'index.html')

def chat(request):  
    if request.method == 'POST':
        user_input = request.POST.get("user_input").decode('utf-8')
        # Process user input and generate response
        response = generate_response(user_input)
        # Save the chat conversation to the database
        chat_entry = ChatEntry(user_input=user_input, response=response)
        chat_entry.save()
        # Pass the response to the frontend
        context = {
            "user_input": user_input,
            "response": response
        }
        return render(request, 'chat.html', context)
    else:
        return render(request, 'chat.html')
   
def projects(request):
    return render(request, 'projects.html')

