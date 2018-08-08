# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from pricing.models import Part
from pricing.serializers import PartSerializer


# Create your views here.
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def price(request):
   # """
   # List all parts, or create a new instance.
   # """
    #if request.method == 'GET':
    #    series = Serie.objects.all()
     #   serializer = SerieSerializer(series, many=True)
      #  return JSONResponse(serializer.data)

	if request.method == 'POST':
		data=list() 
		serializer = list()
		aux = JSONParser().parse(request)
		for i in range(len(aux)):

			#data[i] = aux[i]  #JSONParser().parse(request[i])
        		serializer[i] = PartSerializer(data=aux[i])
        		if serializer[i].is_valid():
            			serializer[i].save()
            			return JSONResponse(serializer.data, status=201)
        		return JSONResponse(serializer.errors, status=400)
