"""sidechain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView
from django.conf import settings
from core import views 
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('core.urls')),
    path('', RedirectView.as_view(url='/posts/', permanent=True)),
    re_path(r'^accounts/', include('registration.backends.default.urls')),
    path('users/<str:username>/', views.profile, name='profile_page'),
    path('tags/', views.tags, name='tags'),
    re_path(r'^(?P<slug>[-\w]+)/comment/$', views.add_comment, name='add_comment'),
    re_path(r'^search/$', views.search, name='search')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
