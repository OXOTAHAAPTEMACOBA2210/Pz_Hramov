from django.db import models
from django.urls import reverse

class Faculty(models.Model):
    name = models.CharField(max_length=100, verbose_name="Факультет")
    description = models.TextField(verbose_name="Описание", blank=True)

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('faculty_detail', args=[str(self.id)])


class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название группы")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name="Факультет", related_name='groups')

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group_detail', args=[str(self.id)])


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    position = models.CharField(max_length=100, verbose_name="Должность")

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def get_absolute_url(self):
        return reverse('teacher_detail', args=[str(self.id)])


class Discipline(models.Model):
    name = models.CharField(max_length=100, verbose_name="Дисциплина")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Преподаватель", related_name='disciplines')
    description = models.TextField(verbose_name="Описание", blank=True)

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('discipline_detail', args=[str(self.id)])


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа", related_name='students')
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="Дата зачисления")
    email = models.EmailField(verbose_name="Email")

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.group})"

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])
