import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import index as core_index
from {{ cookiecutter.initial_app_name }}.views import index as {{ cookiecutter.initial_app_name }}_index

urlpatterns = [
    path('', core_index, name='index'),
    path('{{ cookiecutter.initial_app_name }}/', {{ cookiecutter.initial_app_name }}_index, name='{{ cookiecutter.initial_app_name }}'),

    path('admin/', admin.site.urls),
{% if cookiecutter.use_allauth %}
    # allauth
    path('accounts/', include('allauth.urls')),
{% endif %}
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
