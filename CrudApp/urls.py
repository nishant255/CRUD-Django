from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^home/$',views.home,name='home'),
    url(r'^home/post/$',views.person_post,name='person_post'),
]