
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from pricing.models import Prices

# Register your models here.
class PricingAdmin(admin.ModelAdmin):
	list_display = ('alpi1','alpi2','contrach')

admin.site.register(Prices, PricingAdmin)
