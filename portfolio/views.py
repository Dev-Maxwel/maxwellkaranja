from django.shortcuts import render
from .models import emailingInfo

def index(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        email = request.POST.get("email")
        # Save the emailsending details to the database
        emailInfo = emailingInfo(name=name, phone=phone, email=email, message=message)
        emailInfo.save()    
    else:
        pass           
    return render(request, 'index.html')

