from rest_framework import serializers
from .models import Prices
import ModelSerializer

class PricesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Prices
		fields = ('id','alpi1','alpi2','alpi3','alpi4','alpi5','alpi6','alpi7','alpi8','alpi9','alpi10','alpi11','contrach','prmt','qmm','dmm','tmm','T1','T2','T3','T4','T5','T6','P1','P2','P3','P4','P5')
