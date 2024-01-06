from django.shortcuts import render
from .models import emailingInfo
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    #sending mail
    if request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        email = request.POST.get("email")
        
        #send_mail function parameters
        send_mail(
            f"Message from {name}",
            f"{message}\n\nSender's Name: {name}\nPhone: {phone}\nEmail: {email}",
            email,  # Use the correct variable for sender's email
            ['developermaxwellkaranja@gmail.com'],  # Use the correct variable for recipient's email
            fail_silently=False,
        )

        # Save the email sending details to the database
        emailInfo = emailingInfo(name=name, phone=phone, email=email, message=message)
        emailInfo.save() 
        return render(request, 'index.html')
    else:
        pass

    return render(request, 'index.html')