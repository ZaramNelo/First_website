from django.core.mail import send_mail

def send_reminder_email(fullname,to_email, appointment_time):
    send_mail(
        subject='Appointment Reminder',
        message=f'Hi {fullname}! \nJust a reminder that your appointment is scheduled for {appointment_time}.',
        from_email='zaramboy2017@gmail.com',
        recipient_list=[to_email],
        fail_silently=False,
    )