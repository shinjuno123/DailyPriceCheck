from django.shortcuts import render
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.http import HttpResponse
from .tasks import my_task
# Create your views here.

def index(request):
    my_task.delay()
    return HttpResponse("Task scheduled")

def schedule_task(request):
    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=30,
        period=IntervalSchedule.SECONDS
    )

    PeriodicTask.objects.update_or_create(
        interval=schedule,
        name="my-schedule",
        task="crawler.tasks.my_task",
        # args=json.dump(["Arg1","Arg2"])
        # one_off=True
    )

    return HttpResponse("Task scheduled")