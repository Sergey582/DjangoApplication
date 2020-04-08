from django.conf.urls import url
from . import views
from django.urls import path, include
urlpatterns = [

    # sessions
    path('', include('django.contrib.auth.urls')),
    # register
    url(r'^register/$', views.RegisterView.as_view(), name='register'),

]
