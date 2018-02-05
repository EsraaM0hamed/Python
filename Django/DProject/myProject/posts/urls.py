from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list_view, name='post_list_view'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/'
        r'(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.post_detail_view, name='post_detail_view'),
    url(r'^create/$', views.post_create, name='create_post'),
    url(r'^update/(?P<post_id>\d+)/$', views.post_update, name='post_update'),
    url(r'^delete/(?P<post_id>\d+)/$', views.post_delete, name='post_delete'),
    url(r'^your-name/$', views.get_name, name='your-name'),

]