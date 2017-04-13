from django.conf.urls import url

from . import views

app_name = 'collegeData'
urlpatterns = [
   url(r'^addcollege/$', views.CollegeListV1_0.as_view()),
   url(r'^searchstate/$', views.StateListV1_0.as_view()),
   url(r'^statedetail/$', views.StateDetailV1_0.as_view()),
   url(r'^statelist/$', views.StateIdListV1_0.as_view()),
   url(r'^collegesearch/$', views.CollegeSearchV1_0.as_view()),
   url(r'^allstates/$', views.AllStateListV1_0.as_view()),

]