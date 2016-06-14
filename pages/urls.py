from django.conf.urls import patterns, include, url

from api import views as view

urlpatterns = [
	url(r'', view.index, name='index')
]