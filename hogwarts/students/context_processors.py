from .models import Student, Teacher, Group, Faculty, Discipline

def counts(request):
    """
    Контекстный процессор для предоставления счетчиков объектов
    во всех шаблонах (для сайдбара и бейджей).
    """
    return {
        'num_students': Student.objects.count(),
        'num_teachers': Teacher.objects.count(),
        'num_groups': Group.objects.count(),
        'num_faculties': Faculty.objects.count(),
        'num_disciplines': Discipline.objects.count(),
    }
