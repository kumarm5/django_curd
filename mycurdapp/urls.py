from django.conf.urls import url
from mycurdapp import views

urlpatterns = [
    url(r'^home/$', views.home, name='index' ),
    url(r'^create/$', views.create, name='create'),
    url(r'^update/(?P<id>\d+)/$', views.update, name='update'),
    url(r'delete/(?P<id>\d+)/$', views.delete, name='delete'),    
]