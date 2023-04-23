from datetime import timedelta, datetime

import pytz
from django.core.management.base import BaseCommand

from accounts.models import OtpCode


class Command(BaseCommand):
    help = "remove all expired otp code"

    def handle(self, *args, **options):
        expired_time = datetime.now(tz=pytz.timezone("Asia/Tehran")) - timedelta(minutes=2)
        OtpCode.objects.filter(created__lt=expired_time).delete()
        self.stdout.write("all expired otp deleted successfuly")
