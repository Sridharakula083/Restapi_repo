from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import JsonResponse
def emp_data_jsonview(request):
    emp_data = {'eno':101,'ename':'Rahul','esal':120000,'eaddr':'Hyderabad'}
    return JsonResponse(emp_data)
from django.views.generic import View
import json
class JsonCbv(View):
    def get(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':'This is from get method'})
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':'This is from post method'})
        return HttpResponse(json_data,content_type='application/json')


