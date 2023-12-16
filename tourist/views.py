from .forms import ContactForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            user_email = form.cleaned_data['email']

            form.save()

            message = "New Contact Form Submission\n\n"
            for field, value in form.cleaned_data.items():
                message += f"{field.capitalize()}: {value}\n"

            # Send email notification
            send_mail(
                'New Contact Form Submission',
                message,
                'iamparasghimire@gmail.com',  # Replace with your email
                ['iamparasghimire@gmail.com'],  # Replace with recipient email(s)
                fail_silently=False,
            )

            return redirect('/')  # Redirect to a success page

 
    else:
        form = ContactForm()

    return render(request, "tourist/index.html", {'form': form})