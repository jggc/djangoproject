from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from django.conf import settings
from django.contrib import admin
from filebrowser.sites import site as filebrowsersite

urlpatterns = [
    # Examples:
    # url(r'^$', 'companydotcom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/filebrowser/', include(filebrowsersite.urls)),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    url(r'^', include("website.urls", namespace="website")),
)