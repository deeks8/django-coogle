from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^version1.0/college/', include('collegeData.urls')),
url(r'^version1.0/auth/', include('authenticate.urls')),
    ]