from django_cron import cronScheduler, Job, HOUR, DAY, WEEK, MONTH
from .models import Campaign


class DeleteMe(Job):
    run_every = HOUR/60

    def job():
        obj = Campaign.objects.get(name='deletme')
        obj.delete()

cronScheduler.register(DeleteMe)
