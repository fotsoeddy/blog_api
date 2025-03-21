from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Comment

@receiver(post_save, sender=Comment)
def send_comment_notification(sender, instance, created, **kwargs):
    if created:
        subject = f'New Comment on Your Post: {instance.post.title}'
        message = f'{instance.author.username} commented: {instance.content}'
        recipient_list = [instance.post.author.email]
        send_mail(subject, message, 'your-email@gmail.com', recipient_list)