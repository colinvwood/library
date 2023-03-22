# ----------------------------------------------------------------------------
# Copyright (c) 2018-2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from django import http

from ...packages.models import Package


def list_packages(request):
    if request.method != 'GET':
        payload = {
            'status': 'error',
            'errors': {'http_method': 'invalid http method'}
        }
        return http.JsonResponse(payload, status=405)

    payload = {
        'packages': {
            pkg.name: pkg.repository for pkg in Package.objects.all()
        }
    }
    return http.JsonResponse(payload, status=200)
