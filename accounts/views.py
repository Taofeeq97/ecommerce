from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
# Create your views here.


@csrf_protect
def register(request):

    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username=email.split('@')[0]

            user=Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, username=username)
            user.phone_number=phone_number
            user.save()

            current_site=get_current_site(request)
            mail_subject= 'Please Activate your Account'
            message=render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email=email
            send_email=EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Account creation successful, Please check your email to verify your account')

            return redirect('accounts/login/?command=verification&email='+ email)

    else:
        form=RegistrationForm()
    context={
        'form':form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password = request.POST['password']


        user=auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            #messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request,'Invalid login details')
            return redirect('login')
    return render(request,'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out')
    return redirect('login')

def activate(request, uidb64, token):
    try:
        uidb=urlsafe_base64_decode(uidb64).decode()
        user=Account._default_manager.get(pk=uidb)

    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user=None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active=True
        user.save()
        messages.success(request, 'Yeeehhh!, your account is activated')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')