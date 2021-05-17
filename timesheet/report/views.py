from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.utils import timezone
from datetime import datetime

from .models import User, TimeSheet


def data(request, id,start_date = None, end_date=None):
    user = User.objects.get(user_id=id)
    cols = [
        "",
        "Time",
        "Terminal_id",
        "User_id",
        "Name",
        "Class",
        "Mode",
        "Result",
        "Property",
    ]
    query = TimeSheet.objects.filter(user=user)

    end_date = end_date or timezone.now()
    if start_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        query = query.filter(time__gt=start_date)
    if end_date:
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

        query = query.filter(time__lte=end_date)

    return render(
        request, "data.html", {"user": user, "cols": cols, "times": query.all()}
    )


def index(request):
    return render(request, "user.html")