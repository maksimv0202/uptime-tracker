from django.contrib import admin
from django.urls import include, path

from .handlers import (ExceptionHandler400, ExceptionHandler403,
                       ExceptionHandler404, ExceptionHandler500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('users.urls')),
]

handler400 = ExceptionHandler400.as_view()
handler403 = ExceptionHandler403.as_view()
handler404 = ExceptionHandler404.as_view()
handler500 = ExceptionHandler500.as_view()
