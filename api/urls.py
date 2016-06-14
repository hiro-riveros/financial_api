from django.conf.urls import url, include
from rest_framework import routers
from api import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'', views.index, name='index')
  # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]