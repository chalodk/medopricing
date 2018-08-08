from django.conf.urls import url
from pricing import views

urlpatterns = [
	url(r'^pricing/$', views.price),
]
