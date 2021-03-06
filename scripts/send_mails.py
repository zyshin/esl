from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from registration.models import RegistrationProfile
from django.core.mail import EmailMultiAlternatives, send_mail
import time


def send_activation_prompt_emails(receivers, interval=120):
    settings.ACTIVATION_EMAIL_HTML = 'registration/activation_prompt_email.html'
    site = get_current_site(None)
    for receiver in receivers:
        profile = RegistrationProfile.objects.get(user__email=receiver)
        RegistrationProfile.objects.resend_activation_mail(profile.user.email, site)
        time.sleep(interval)
    del settings.ACTIVATION_EMAIL_HTML

def send_emails(subject, message_txt, message_html, receivers, interval=120):
    from_email = getattr(settings, 'REGISTRATION_DEFAULT_FROM_EMAIL', settings.DEFAULT_FROM_EMAIL)
    for receiver in receivers:
        print 'Send to ', receiver, ':', send_mail(subject, message_txt, from_email, [receiver], html_message=message_html)
        time.sleep(interval)
