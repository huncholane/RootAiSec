from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@staff_member_required
def logs(request):
    return render(request, 'live_logger/logs.html', {
    })