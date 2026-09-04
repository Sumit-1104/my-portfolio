from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from.models import*

# Create your views here.

def index(request):
    about=About.objects.all()
    skills=Skills.objects.all()
    education=Education.objects.all()
    experience=Experience.objects.all()
    port = portfolio.objects.filter(is_published=True)
    service=Service.objects.all()

    return render(request, 'index.html', {
        'about': about,
        'skills': skills,
        'education': education,
        'experience': experience,
        'port': port,
        'service': service,
    })


@require_POST
def contact(request):
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    subject = request.POST.get('subject', '').strip()
    message = request.POST.get('message', '').strip()

    if not all((name, email, subject, message)):
        return HttpResponse('Please complete all fields.', status=400)

    EmailMessage(
        subject,
        f'From: {name} <{email}>\n\n{message}',
        settings.DEFAULT_FROM_EMAIL,
        [settings.CONTACT_EMAIL],
        reply_to=[email],
    ).send()
    return HttpResponse('OK')
