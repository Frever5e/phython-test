"""
WSGI config for django_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import pymysql
conn = pymysql.connect(host='localhost', user='root', password='1234', db='kjhdb', charset='utf8')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_test.settings')

application = get_wsgi_application()

# git test