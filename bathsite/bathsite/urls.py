from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'bathsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^', include('treegenerator.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
