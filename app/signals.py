from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post
from django.conf import settings

@receiver(post_save, sender=Post)
def send_notification_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New Post Created'
        message = f'Your new post "{instance.title}" has been created.'
        from_email = "" # Update with your email
        recipient_list = [instance.author.email]
        send_mail(subject, message, from_email, recipient_list)
