from rest_framework import serializers
from .models import Part


class PartSerializer(serializers.Serializer):

	pk = serializers.IntegerField(read_only=True)
	thickness = serializers.FloatField()
	area = serializers.FloatField()
	perimeter = serializers.FloatField()
	quantity = serializers.IntegerField()
	veneer = serializers.ChoiceField(choices=Part.VENEER_CHOICES)
	name = serializers.ChoiceField(choices=Part.PART_CHOICES)
	
	def create(self, validated_data):
		"""
        	Create and return a new `Part` instance, given the validated data.
		"""
		return Part.objects.create(**validated_data)

	def update(self, instance, validated_data):
        
        
		instance.name = validated_data.get('name', instance.name)
		instance.thickness = validated_data.get('thickness', instance.thickness)
		instance.area = validated_data.get('area', instance.area)
		instance.perimeter = validated_data.get('perimeter', instance.perimeter)
		instance.quantity = validated_data.get('quantity', instance.quantity)
		instance.veneer = validated_data.get('veneer', instance.veneer)

		instance.save()
		return instance
