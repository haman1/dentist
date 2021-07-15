from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        comments = request.POST['comments']
        
        ### send mail
        send_mail(
            name,
            email,
            comments,
            ['githigithia@gmail.com'],
        )

        return render(request, 'home.html', {'name': name})
    else:
        return render(request, 'home.html', {})




