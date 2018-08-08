# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Part(models.Model):

	TABLERO = 'tablero'
	UNION = 'union'
	APOYOS = 'apoyos'

	PART_CHOICES = (
		(TABLERO, 'Tablero'),
		(UNION, 'Union'),
		(APOYOS, 'Apoyos'),
	)


	ALPI1 = 'alpi1'
	ALPI2 =	'alpi2'
	ALPI3 =	'alpi3'
	ALPI4 =	'alpi4'
	ALPI5 =	'alpi5'
	ALPI6 =	'alpi6'
	ALPI7 =	'alpi7'
	ALPI8 =	'alpi8'
	ALPI9 =	'alpi9'
	ALPI10 = 'alpi10'
	ALPI11	= 'alpi11'
	CONTRACHAPA = 'contrach'


	VENEER_CHOICES = (
		(ALPI1, 'alpi1'),
		(ALPI2,	'alpi2'),
		(ALPI3,	'alpi3'),
		(ALPI4,	'alpi4'),
		(ALPI5,	'alpi5'),
		(ALPI6,	'alpi6'),
		(ALPI7,	'alpi7'),
		(ALPI8,	'alpi8'),
		(ALPI9,	'alpi9'),
		(ALPI10, 'alpi10'),
		(ALPI11, 'alpi11'),
		(CONTRACHAPA, 'contrach'),
	)


	name = models.CharField(max_length=10, choices = PART_CHOICES)
	thickness = models.FloatField(default=0)
	area = models.FloatField(default=0)
	perimeter = models.FloatField(default=0)
	quantity = models.IntegerField(default=1)
	veneer = models.CharField(max_length=15, choices = VENEER_CHOICES)


#class Design(models.Model):

	
