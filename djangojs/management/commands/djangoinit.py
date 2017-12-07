# -*- coding: utf-8 -*-
import os
import sys

from django.conf import settings
from django.core import urlresolvers
from django.core.exceptions import ImproperlyConfigured
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.core.management.base import BaseCommand
from django.test.client import RequestFactory


class Command(BaseCommand):
    help = 'create django js init file'

    def get_location(self):
        import djangojs
        path = os.path.dirname(djangojs.__file__)
        return os.path.join(path, 'static/js/djangojs')

    def handle(self, *args, **options):
        from djangojs.views import JsInitView

        location = self.get_location()
        file = 'init.js'
        fs = FileSystemStorage(location=location)
        if fs.exists(file):
            fs.delete(file)

        request = RequestFactory().get('/')
        content = JsInitView.as_view()(request, as_string=True)

        fs.save(file, ContentFile(content))
        if len(sys.argv) > 1 and sys.argv[1] in ['create_init_js']:
            self.stdout.write('init.js file written to %s' % (location))  # pragma: no cover
