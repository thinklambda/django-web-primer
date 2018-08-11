'''
Created on 11-Aug-2018

@author: Venkat.Krish
'''
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name="about")
    ]
    
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)