from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta
from Junction_academy.models import Free_trials_list
from Junction_academy.utils import send_reminder_email

class Command(BaseCommand):
     def handle(self, *args, **kwargs):
        tomorrow = now().date() + timedelta(days=1)
        appointments = Free_trials_list.objects.filter(Date=tomorrow)

        for point in appointments:
            send_reminder_email(point.Fullname,point.Email,f"{point.Time.strftime('%H:%M')} {point.Date}")
            self.stdout.write(self.style.SUCCESS(f'Reminder sent to {point.Email}'))