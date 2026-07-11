from django.urls import path

from . import views

app_name = "marketing"

urlpatterns = [
    # Main pages
    path("", views.HomeView.as_view(), name="home"),
    path("features/", views.FeaturesView.as_view(), name="features"),
    path("pricing/", views.PricingView.as_view(), name="pricing"),
    path("why-us/", views.WhyUsView.as_view(), name="why_us"),
    path("demo/", views.DemoView.as_view(), name="demo"),
    path("case-studies/", views.CaseStudiesView.as_view(), name="case_studies"),
    path("documentation/", views.DocumentationView.as_view(), name="documentation"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    # Demo request form submission
    path("request-demo/", views.RequestDemoView.as_view(), name="request_demo"),
]
