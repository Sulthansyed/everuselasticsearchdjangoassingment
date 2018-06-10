from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.display, name='all_list'),
    url(r'^$', views.user1, name='user1'),
    url(r'^$', views.user2, name='user2')

] 
