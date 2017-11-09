from django.shortcuts import render

from django.http import *
from django.views.decorators.http import require_http_methods

from .models import Employee
import time
import json
# Create your views here.

@require_http_methods([ "POST"])
def report(request):
	data = json.loads(request.body)
	auth = data['auth']
	auth_anonymous = data['auth_anonymous']


	employee = Employee(mis = auth ,anonymous = auth_anonymous,time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
	employee.save()
	return HttpResponse('ok')
