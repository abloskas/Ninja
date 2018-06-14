from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_user/?$', views.new_user), 
    url(r'^login/?$', views.login),
    url(r'^strengths/?$', views.strength),
     url(r'^strengths/(?P<id>\d+)?$', views.strength_edit),
    url(r'^socials/?$', views.socials),
    url(r'^socials_process/?$', views.socials_process), 
    url(r'^process/?$', views.process), 
     url(r'^process_edit/?$', views.process_edit), 
    url(r'^home/?$', views.home), 
    url(r'^help_search/?$', views.help_search),
    url(r'^user_search/?$', views.user_search),
    url(r'^searching_user/?$', views.searching_user), 
    url(r'^searching_help/?$', views.searching_help), 
    url(r'^logout/?$', views.logout),
    url(r'^edit/(?P<id>\d+)?$', views.edit), 
    url(r'^profile/(?P<id>\d+)?$', views.profile),
    url(r'^profile/(?P<id>\d+)/edit/?$', views.edit_profile),
    url(r'^map/?$', views.map)
]
