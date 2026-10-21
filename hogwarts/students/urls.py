from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Маршруты-заглушки, ведущие на пустую страницу
    path('students/', views.empty_view, name='students_list'),
    path('teachers/', views.empty_view, name='teachers_list'),
    path('groups/', views.empty_view, name='groups_list'),
    path('faculties/', views.empty_view, name='faculties_list'),
    path('disciplines/', views.empty_view, name='disciplines_list'),
]