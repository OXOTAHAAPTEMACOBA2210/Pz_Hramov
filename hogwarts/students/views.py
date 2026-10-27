from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Student, Teacher, Group, Faculty, Discipline

def index(request):
    """
    Главная страница сайта университета (ПЗ 2, 4, 5).
    """
    context = {
        'num_students': Student.objects.count(),
        'num_teachers': Teacher.objects.count(),
        'num_groups': Group.objects.count(),
        'num_faculties': Faculty.objects.count(),
        'num_disciplines': Discipline.objects.count(),
    }
    return render(request, 'index.html', context)


# --- Представления для Студентов (ПЗ 7) ---
class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    paginate_by = 5  # Усложнение: пагинация по 5 студентов

    def get_queryset(self):
        # Усложнение: поиск студентов по фамилии / имени
        query = self.request.GET.get('q', '').strip()
        qs = Student.objects.select_related('group', 'group__faculty').all()
        if query:
            qs = qs.filter(Q(last_name__icontains=query) | Q(first_name__icontains=query))
        return qs.order_by('last_name', 'first_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '').strip()
        context['total_count'] = Student.objects.count()
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'


# --- Представления для Преподавателей (ПЗ 7) ---
class TeacherListView(ListView):
    model = Teacher
    template_name = 'students/teacher_list.html'
    context_object_name = 'teachers'

    def get_queryset(self):
        return Teacher.objects.prefetch_related('disciplines').all().order_by('last_name', 'first_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_count'] = Teacher.objects.count()
        return context


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'students/teacher_detail.html'
    context_object_name = 'teacher'


# --- Представления для Групп (ПЗ 7) ---
class GroupListView(ListView):
    model = Group
    template_name = 'students/group_list.html'
    context_object_name = 'groups'

    def get_queryset(self):
        return Group.objects.select_related('faculty').prefetch_related('students').all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_count'] = Group.objects.count()
        return context


class GroupDetailView(DetailView):
    model = Group
    template_name = 'students/group_detail.html'
    context_object_name = 'group'


# --- Представления для Факультетов (ПЗ 7) ---
class FacultyListView(ListView):
    model = Faculty
    template_name = 'students/faculty_list.html'
    context_object_name = 'faculties'

    def get_queryset(self):
        return Faculty.objects.prefetch_related('groups').all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_count'] = Faculty.objects.count()
        return context


class FacultyDetailView(DetailView):
    model = Faculty
    template_name = 'students/faculty_detail.html'
    context_object_name = 'faculty'


# --- Представления для Дисциплин (ПЗ 7) ---
class DisciplineListView(ListView):
    model = Discipline
    template_name = 'students/discipline_list.html'
    context_object_name = 'disciplines'

    def get_queryset(self):
        return Discipline.objects.select_related('teacher').all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_count'] = Discipline.objects.count()
        return context


class DisciplineDetailView(DetailView):
    model = Discipline
    template_name = 'students/discipline_detail.html'
    context_object_name = 'discipline'
