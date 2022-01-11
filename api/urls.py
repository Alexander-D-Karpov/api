import secrets
import string

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView

from api import settings

admin_link = ""

if not settings.DEBUG:
    alphabet = string.ascii_letters + string.digits
    admin_link = "".join(secrets.choice(alphabet) for i in range(30))

urlpatterns = (
    [
        path(str("admin" + admin_link + "/"), admin.site.urls),
        path(
            "robots.txt",
            TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        ),
        path(
            "users/",
            include("users.urls"),
        ),
        path(
            "posts/",
            include("blog.urls"),
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

if settings.DEBUG:
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)