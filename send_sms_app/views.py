from django.shortcuts import render

from .forms import PhoneForm
from .tasks import send_sms


def send_sms_view(request):
    if request.method == "GET":
        form = PhoneForm()
        return render(request, 'send_sms_app/sms.html', {'form': form})

    form = PhoneForm(request.POST)
    if form.is_valid():
        receiver = form.cleaned_data['phone']
        message = form.cleaned_data['message']
        send_sms.delay(receiver, message)

    return render(request, 'send_sms_app/sms.html', {'form': form})

