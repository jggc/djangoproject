__author__ = 'jgcouture'

from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name="homepage"),
    url(_(r'^about/$'), views.AboutView.as_view(), name="about"),
]

