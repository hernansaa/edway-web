from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.urls import include, path
from pathlib import Path


def serve_static_file(filepath: str):
    def view(request: HttpRequest) -> HttpResponse:
        full_path = settings.STATIC_ROOT / filepath
        if not full_path.exists():
            full_path = Path(settings.STATICFILES_DIRS[0]) / filepath
        content = full_path.read_bytes()
        content_type = "text/plain" if filepath.endswith(".txt") else "application/xml"
        return HttpResponse(content, content_type=content_type)

    return view


urlpatterns = [
    path("robots.txt", serve_static_file("robots.txt")),
    path("sitemap.xml", serve_static_file("sitemap.xml")),
    path("", include("apps.marketing.urls")),
]
