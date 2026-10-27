from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),

    # Студенты (поддерживаем оба варианта имени: student_list и students_list)
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/', views.StudentListView.as_view(), name='students_list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),

    # Преподаватели
    path('teachers/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers_list'),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),

    # Группы
    path('groups/', views.GroupListView.as_view(), name='group_list'),
    path('groups/', views.GroupListView.as_view(), name='groups_list'),
    path('groups/<int:pk>/', views.GroupDetailView.as_view(), name='group_detail'),

    # Факультеты
    path('faculties/', views.FacultyListView.as_view(), name='faculty_list'),
    path('faculties/', views.FacultyListView.as_view(), name='faculties_list'),
    path('faculties/<int:pk>/', views.FacultyDetailView.as_view(), name='faculty_detail'),

    # Дисциплины
    path('disciplines/', views.DisciplineListView.as_view(), name='discipline_list'),
    path('disciplines/', views.DisciplineListView.as_view(), name='disciplines_list'),
    path('disciplines/<int:pk>/', views.DisciplineDetailView.as_view(), name='discipline_detail'),
]
