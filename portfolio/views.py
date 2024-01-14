from django.shortcuts import render
from .models import emailingInfo
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def home(request):
    #sending mail
    if request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("subject")
        message = request.POST.get("message")
        email = request.POST.get("email")
        
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


def sitemap(request):
    sitemap_content = (
        "<sitemap> <loc>https://www.maxwellkaranja.me</loc>"
        "<lastmod>2024-01-14 T15:00:44Z</lastmod>"
        "</sitemap>"
    )
    return HttpResponse(f"<pre>{sitemap_content}</pre>")