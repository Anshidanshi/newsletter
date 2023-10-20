from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Subscriber,Newsletter
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
def subscribe(request):
    if request.method != 'POST':
        return render(request, 'index.html',)
    email = request.POST.get('email')
    if Subscriber.objects.filter(email=email).exists():
        # You can return an error message or redirect to a different page here
        # For now, let's assume you want to show a message
        return HttpResponse("You are already subscribed!")
    sub = Subscriber.objects.create(
        email=email
    )

    subject = "Welcome to Our Newsletter"
    from_email = "yourmail@gmail.com"  # Replace with your email
    recipient_list = [email]

    # Load your email template
    html_template = get_template('email_template.html')

    # Define context data for your email template
    context = {
        'user_email': email,
        # Add other context data here
    }

    # Render the HTML template with the context
    html_content = html_template.render(context)

    # Create the EmailMultiAlternatives object
    msg = EmailMultiAlternatives(subject, "", from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")

    # Send the email
    msg.send()
    return redirect('thank_you')

def thank_you(request):
    return render(request, 'ta.html')
@user_passes_test(lambda u: u.is_superuser)
def send_newsletter(request):
    if request.method != 'POST':
        return render(request, 'dp.html')
    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.POST.get('img')
    #image = request.FILES.get('img')  # Access the uploaded image
   
    #print(image)
    # Create a Newsletter instance and save it
    newsletter = Newsletter(title=title, content=content, img=image)
     # Save the uploaded image
    newsletter.save()
    subscribers = Subscriber.objects.all()
    subject = "Welcome to Our Newsletter"
    from_email = "yourmail@gmail.com"
    recipient_list = [subscriber.email for subscriber in subscribers]
    html_template = get_template('news.html')

    # Define context data for your email template
    context = {
        'image': image,
        'title': content,
        'hi': title,

    # Add other context data here
    }

    # Render the HTML template with the context
    html_content = html_template.render(context)

    # Create the EmailMultiAlternatives object
    msg = EmailMultiAlternatives(subject, "", from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")

    # Send the email
    msg.send()
    return redirect('thank_you')

def unsubscribe(request, pk):
    subscribe = Subscriber.objects.filter(email=pk).first()
    subscribe.delete()
    return HttpResponseRedirect('/unsubscribed/')
def unsubscribed(request):
    
    return render(request,'unsubscribed.html')

