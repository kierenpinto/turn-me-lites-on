from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views
import main.views
# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', main.views.IndexView.as_view(),name = 'index'),
    url(r'^olddb', hello.views.db, name='old_db'),
    url(r'^old/$', hello.views.index, name='old_index'),
    path(r'admin/', admin.site.urls),
    path(r'home/', include('main.urls')),
]
