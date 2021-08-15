from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls')),
    path('get_api/', include('fapi.urls'), name='get_api'),
    path('admin/', admin.site.urls),
]
