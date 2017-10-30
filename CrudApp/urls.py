from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^create/$', views.create_person, name='create_person'),
    url(r'^person/(?P<pk>\d+)/$', views.get_person, name='get_person'),

]
