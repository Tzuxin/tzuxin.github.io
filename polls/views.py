from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/polls')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect ('login')
    else:
        return render (request, 'login.html')

def logout(request):
    return redirect('/polls/login2')

def counter(request):
    posts = ['tope','kai','maya','jhaz']
    return render(request, 'counter.html', {'posts': posts})

def post(request, pk):
    
    return render(request, 'post.html', {'pk': pk})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('polls:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('polls:signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                email_subject = 'TEST'
                message = 'Hello! Have you receive the message?'
                email_address = email
                try:
                    
                    send_mail(
                        email_subject,
                        message = message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[email_address],
                        fail_silently=False,
                    )
                except Exception:
                    import logging
                    logger = logging.getLogger('django.request')
                    # logger.error(extra={'request': request}) or logger.exception()
                    messages.error(
                        'There might be a problem in sending the email. ',
                    )
                return redirect('polls:login2')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('polls:signup')
    else:
        return render(request, 'signup.html')

def delete_user(request, username):
    username = str(username)
    try:
        userDel = User.objects.get(username = username)
        print (userDel)
    except User.DoesNotExist:
        return redirect('polls:signup')
    userDel.delete()
    return redirect('signup')
    

def login2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        message = 'Hello! Have you receive the message?'
        
        mail_1 = (
            'Test mass mail!',
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['bicol.u.pc@gmail.com', 'researcher.gulai@gmail.com'],
        )
        mail_2 = (
            'Testin send_mass_mail!',
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['bicol.u.pc@gmail.com', 'researcher.gulai@gmail.com'],
        )

        send_mass_mail((mail_1, mail_2),fail_silently=False)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect ('polls:login2')
    else:
        return render (request, 'login2.html')


# class EmailTest(TestCase):
#     def test_send_email(self):
#         # Send message.
#         mail.send_mail('Subject here', 'Here is the message.',
#             'from@example.com', ['to@example.com'],
#             fail_silently=False)

#         # Test that one message has been sent.
#         self.assertEqual(len(mail.outbox), 1)

#         # Verify that the subject of the first message is correct.
#         self.assertEqual(mail.outbox[0].subject, 'Subject here')