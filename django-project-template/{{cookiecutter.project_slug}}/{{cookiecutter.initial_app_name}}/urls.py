import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import index as {{ cookiecutter.initial_app_name }}_index
{%- if cookiecutter.include_test_app %}
from test_app.views import index as test_app_index
{%- endif %}

urlpatterns = [
    path('', {{ cookiecutter.initial_app_name }}_index, name='index'),
{%- if cookiecutter.include_test_app %}
    path('test_app/', test_app_index, name='test_app'),
{%- endif %}

    path('admin/', admin.site.urls),
{% if cookiecutter.use_allauth %}
    # allauth
    path('accounts/', include('allauth.urls')),
{% endif %}
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
