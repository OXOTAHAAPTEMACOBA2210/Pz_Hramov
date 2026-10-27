from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Основные маршруты портала университета
    path('', include('students.urls')),
    # Префиксное подключение для обратной совместимости с ПЗ 2
    path('students/', include('students.urls')),
]
