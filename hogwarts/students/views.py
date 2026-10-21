from django.shortcuts import render
from .models import Student, Teacher, Group, Faculty, Discipline

def index(request):
    # Подсчитываем количество записей в каждой таблице
    context = {
        'num_students': Student.objects.count(),
        'num_teachers': Teacher.objects.count(),
        'num_groups': Group.objects.count(),
        'num_faculties': Faculty.objects.count(),
        'num_disciplines': Discipline.objects.count(),
    }
    # Передаем словарь context в шаблон index.html
    return render(request, 'index.html', context)

# Функции-заглушки для пустых страниц
def empty_view(request):
    return render(request, 'empty.html')