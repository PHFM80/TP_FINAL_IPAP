from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/sustentabilidad/', permanent=False)),
    path('', include('ejercicio_3_auditoria_web.urls')),
]