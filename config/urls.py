from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView, RedirectView

from django.conf import settings
import debug_toolbar
import logging

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/', include('apiv1.urls')),
    re_path('', RedirectView.as_view(url='/')),
]

if settings.DEBUG:
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns

    logger = logging.getLogger(__name__)
    logger.info('config urls')
