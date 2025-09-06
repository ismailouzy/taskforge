from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_welcome_email(email):
    """
    Async Celery task to send welcome email.
    """
    subject = 'Welcome to TaskForge!'
    message = 'Thank you for registering. Start managing your tasks now!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
