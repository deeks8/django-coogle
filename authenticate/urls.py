from django.conf.urls import url

from . import views

app_name = 'authenticate'
urlpatterns = [
   url(r'^register/$', views.RegisterUser.as_view()),
   url(r'^login/$', views.LoginListV1_0.as_view()),
   ]