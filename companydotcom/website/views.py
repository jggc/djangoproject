from django.shortcuts import render
from django.views import generic
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    """ Try to translate a string bob """
    print(request)
    output = _("Let's translate this in %(lang)s") % {'lang': request.LANGUAGE_CODE}
    return HttpResponse(output)


class AboutView(generic.TemplateView):
    """
    About company page
    """
    template_name = 'website/about.html'