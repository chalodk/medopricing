# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from inteligencia import precio_mueble
from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from pricing.models import Prices
from pricing.serializers import PricesSerializer


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
	#"""
	#List all parts, or create a new instance.
	#"""
	if request.method == 'GET':
		aux = Prices.objects.all()
        serializer1 = PricesSerializer(aux)
        params = JSONParser().parse(request) ## dict con los parametros
        prices = serializer1.data ### dict con los precios
        final = precio_mueble(params, prices)
        serializer2 = FinalSerializer(data=final) ## generando instancia
        aux2 = serializer2.save() ## Guardando instancia
        serializer3 = FinalSerializer(Final.objects.all())
        precio_final = serializer3.data ## Carga la data del modelo "Final"
        
        
        return JSONResponse(precio_final)
		
        
       
        
		#aux = JSONParser().parse(request)
		#dicc = serializer.data
		#precio = {'tablero':0,'union':0, 'apoyos':0}
		#for i in aux:
	#		precio[i] = precio[i]+(dicc[aux[i]['veneer']]+dicc[aux[i]['width']])*aux[i]['area']+dicc['prmt']*aux[i]['prmt']
		#precio['final']=precio['tablero']+precio['union']+precio['apoyos']
		#return JSONResponse(serializer.data)

	#if request.method == 'POST':
	#	data=list() 
	#	serializer = list()
	#	aux = JSONParser().parse(request)
	#	for i in range(len(aux)):

			#data[i] = aux[i]  #JSONParser().parse(request[i])
        #		serializer[i] = PartSerializer(data=aux[i])
        #		if serializer[i].is_valid():
         #   			serializer[i].save()
          #  			return JSONResponse(serializer.data, status=201)
        #		return JSONResponse(serializer.errors, status=400)
