from django.http import HttpResponse
from django.shortcuts import render, redirect

from client.forms import ContactForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

# def about(request):
#     return HttpResponse("This is the About Page")

def features(request):
    return render(request,'features.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Send email
            # send_email(
            #     subject=f"New contact form submission: {form.cleaned_data['subject']}"
            #     message=form.cleaned_data['message'],
            #     from_email=form.cleaned_data['from_email'],
            #     recipient_list=['johnmaneene@gmail.com'],
            # )
            messages.success(request, 'Thank you for reaching out!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request,'contact.html',{'form':form})