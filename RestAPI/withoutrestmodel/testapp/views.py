from django.shortcuts import render
from django.views.generic import View
import json
from testapp.models import Employee
from django.http import HttpResponse
from django.core.serializers import serialize
from testapp.mixins import SerializeMixin,HttpResponseMixin

# Create your views here.
class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The requested resource is not available'})
            return self.render_http_Response(json_data,status=404)
        else:
            json_data = serialize('json',[emp,])
            return HttpResponse(json_data,content_type='application/json',status=200)


class EmployeeListCBV(SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data,content_type='application/json')
