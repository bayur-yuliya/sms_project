1. Install deps
```
pip install -r requirements.txt
```
2.  Run broker
```
docker run -d -p 5672:5672 rabbitmq
```
3. Set your TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN  environment variables

Mac & Linux
```
export TWILIO_ACCOUNT_SID='ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
export TWILIO_AUTH_TOKEN='your_auth_token'
```
Windows
```
set TWILIO_ACCOUNT_SID=ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set TWILIO_AUTH_TOKEN=your_auth_token
```
4. Run worker process
```
celery -A sms_project worker -l INFO 
```
Run worker process in windows
```
celery -A sms_project worker -l INFO --pool=solo
```
4. Run Django web-server
```
python manage.py runserver
```