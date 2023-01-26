from django.contrib import admin
from django.urls import path, re_path, include
from applications.persona.urls import personas_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/',include(personas_patterns))
]
