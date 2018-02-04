from django.conf.urls import url 
from . import views


urlpatterns=[
    url(r'^$',views.post_lists_view,name='post_lists_view'),
    
    




]