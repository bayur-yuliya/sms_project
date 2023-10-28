from celery import shared_task
from twilio.rest import Client

from sms_project import settings

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


@shared_task
def send_sms(receiver, message):
    message = client.messages \
        .create(
        body=message,
        from_='+14098774336',
        to=receiver,
    )
    return message.sid
