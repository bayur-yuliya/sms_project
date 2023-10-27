from django.shortcuts import render
from tasks import send_sms

def send_sms_view(request):
    send_sms.delay(4, 4)

