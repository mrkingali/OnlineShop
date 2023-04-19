from django.core.management.base import BaseCommand
from datetime import timedelta,datetime
from accounts.models import OtpCode


class Command(BaseCommand):
    help = "remove all expired otp code"
    def handle(self, *args, **options):
        expired_time=datetime.now()-timedelta(minutes=2)
        OtpCode.objects.filter(created__lt=expired_time).delete()
        self.stdout.write("all expired otp deleted successfuly")