from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.

def index(request):
    if request.method == "POST":
        your_name = request.POST.get("your-name")
        your_email = request.POST.get("your-email")

        send_mail(
            f"Hello, {your_name}",
            "Hello Inside a message",
            "emailfromsettings@gmail.com",
            [your_email],
            fail_silently=False
        )

    return render(request, 'main/index.html', {})
