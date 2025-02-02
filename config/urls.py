# ----------------------------------------------------------------------------
# Copyright (c) 2018-2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from library.index import views as index_views
from library.sso import views as sso_views


urlpatterns = [
    path('', index_views.IndexView.as_view(), name='index'),
    path('_debug', index_views.debug_celery_view),
    path('about/', index_views.AboutView.as_view(), name='about'),
    path('plugins/', include(('library.plugins.urls', 'plugins'))),
    path('api/v1/', include('library.api.urls', 'api')),
    path('admin/', admin.site.urls),
]

# Debug toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += [
        path('login/', RedirectView.as_view(pattern_name='admin:login', query_string=True), name='login'),
        path('logout/', RedirectView.as_view(pattern_name='admin:logout', query_string=True), name='logout'),
    ]

else:
    urlpatterns += [
        path('login/', sso_views.sso_redirect_to_provider, name='login'),
        path('login/callback/', sso_views.sso_client_callback, name='sso_callback'),
        path('logout/', sso_views.sso_client_logout, name='logout'),
    ]
