"""
URL configuration for meiduo_mall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from django.http import HttpResponse
# def log(request):
#     import logging
#     logger = logging.getLogger('django')
#     logger.info('user login')
#     logger.warning('redis insufficient cache')
#     logger.error('thie record doesn\'t exist')
#     logger.debug('~~~~~~~')
#     return HttpResponse('log')

# registration converter
from utils.converters import UsernameCountConverter
from django.urls import register_converter

register_converter(UsernameCountConverter, 'username')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path('', include('apps.verifications.urls')),
]
