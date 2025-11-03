import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from {{ cookiecutter.initial_app_name }}.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
{% if cookiecutter.use_allauth %}
    # allauth
    path('accounts/', include('allauth.urls')),
{% endif %}
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
