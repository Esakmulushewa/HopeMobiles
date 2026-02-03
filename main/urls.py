from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('screens/<int:screen_id>/', views.details, name="details"),
    path('phones/<str:phone_type>', views.types, name="phone_type"),
    path('screens/', views.screens, name="screens"),
    path("results", views.results, name="results"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)