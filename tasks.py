from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def send_sms(phone, message):
    pass
    # return