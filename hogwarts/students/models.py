from django.db import models
from django.urls import reverse

class Faculty(models.Model):
    name = models.CharField(max_length=100, verbose_name="Факультет")
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название группы")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name="Факультет")

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    position = models.CharField(max_length=100, verbose_name="Должность")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Discipline(models.Model):
    name = models.CharField(max_length=100, verbose_name="Дисциплина")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name="Преподаватель")

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="Дата зачисления")
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.group})"

    def get_absolute_url(self):
        # Шаблон ссылки на профиль студента (пока самой страницы нет, но метод готов)
        return reverse('student-detail', args=[str(self.id)])