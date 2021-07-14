# ----------------------------------------------------------------------------
# Copyright (c) 2018-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import shlex
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload


def run_cmd(cmd):
    split_cmd = shlex.split(cmd)
    subprocess.run(split_cmd)


def restart_celery_beat():
    run_cmd('pkill -f "celery worker"')
    run_cmd('celery -A config.celery beat')


class Command(BaseCommand):
    def handle(self, *args, **options):
        autoreload.run_with_reloader(restart_celery_beat)
