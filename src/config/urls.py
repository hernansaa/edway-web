from django.urls import include, path

urlpatterns = [
    path("", include("apps.marketing.urls")),
]
