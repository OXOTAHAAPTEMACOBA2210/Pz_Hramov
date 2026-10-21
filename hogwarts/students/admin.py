from django.contrib import admin
from .models import Faculty, Group, Teacher, Discipline, Student

admin.site.register(Faculty)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Discipline)
admin.site.register(Student)