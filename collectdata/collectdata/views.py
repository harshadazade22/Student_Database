from django.http import HttpResponse
from django.shortcuts import render
from formdata.models import Saveform
from django.core.mail import send_mail
def Savedata(request):
    if request.method=="POST":
              
        name=request.POST.get('NAME')
        email=request.POST.get('EMAIL')
        moblie=request.POST.get('MobileNo')
        address=request.POST.get('ADDRESS')
        todata=Saveform(name=name,email=email,moblie=moblie,address=address)
        todata.save()

    return render(request,"contact.html")

def homepage(request):
    #sytanx:
#     send_mail(
#     "Subject here",
#     "Here is the message.",
#     "from@example.com",
#     ["to@example.com"],
#     fail_silently=False,
# )
    send_mail(
    "Sending Email From Django",
    "Welcome to IPCS Global",
    "hzade22@gmail.com",
    ["harshadazade22@gmail.com","shahusejal75@gmail.com","aspatil124@gmail.com","ketki.upase@gmail.com"],
    fail_silently=False,)
    return render(request ,"contact.html")