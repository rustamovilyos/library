from django.urls import path
from .views import BookAPIView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', BookAPIView.as_view(), name='api_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
