from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView 
from accounts.views import SignUpView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # Django's built-in auth URLs
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
]