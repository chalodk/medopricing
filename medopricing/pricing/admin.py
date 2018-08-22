# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from . import models

# Register your models here.
class FeedItemAdmin(admin.ModelAdmin):
  list_display = ('alpi1','alpi2','contrach')
  admin.site.register(models.Prices, PricesAdmin)
