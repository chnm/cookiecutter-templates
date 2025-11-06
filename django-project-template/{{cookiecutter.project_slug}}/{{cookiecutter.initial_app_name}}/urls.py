import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import index as {{ cookiecutter.initial_app_name }}_index
from test_app1.views import index as test_app1_index

urlpatterns = [
    path('', {{ cookiecutter.initial_app_name }}_index, name='index'),
    path('test_app1/', test_app1_index, name='test_app1'),

    path('admin/', admin.site.urls),
{% if cookiecutter.use_allauth %}
    # allauth
    path('accounts/', include('allauth.urls')),
{% endif %}
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
