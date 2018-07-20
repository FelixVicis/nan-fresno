from django.conf.urls import url
from . import views
from django.contrib import admin
admin.site.site_title = "NAN FRESNO"
admin.site.site_header = "NAN ADMINISTRATOR"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>.+)/$', views.details, name='details')
]
