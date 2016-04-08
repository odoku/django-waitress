# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from django.conf import settings
from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.management.base import BaseCommand
from django.core.wsgi import get_wsgi_application
from django.utils import autoreload
from waitress import serve


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--host',
            '-H',
            default=getattr(settings, 'WAITRESS_HOST', '0.0.0.0'),
            type=str,
            help='Server host',
        )

        parser.add_argument(
            '--port',
            '-p',
            default=getattr(settings, 'WAITRESS_PORT', 8000),
            type=int,
            help='Server port',
        )

        parser.add_argument(
            '--noautoload',
            action='store_false',
            dest='autoload',
            default=getattr(settings, 'WAITRESS_AUTOLOAD', True),
            help='Tells Django to NOT use the auto-reloader.',
        )

    def handle(self, *args, **options):
        if options.get('autoload'):
            autoreload.main(self.run, None, options)
        else:
            self.run(*args, **options)

    def get_wsgi_application(self):
        application = get_wsgi_application()
        if settings.DEBUG:
            return StaticFilesHandler(application)
        return application

    def run(self, *args, **options):
        autoreload.raise_last_exception()
        application = self.get_wsgi_application()
        serve(application, host=options.get('host'), port=options.get('port'))
