from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_album/$', views.details, name='details'),
    url(r'^get_songs/$',views.song,name='song'),
]