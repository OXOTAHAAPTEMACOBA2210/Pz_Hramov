# -*- coding: utf-8 -*-
import os, sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def create_doc(pz_number, pz_title, project_name):
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.78)
        s.bottom_margin = Inches(0.78)
        s.left_margin = Inches(0.98)
        s.right_margin = Inches(0.78)
        
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)
    font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    style.paragraph_format.line_spacing = 1.15
    style.paragraph_format.space_after = Pt(4)
    
    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p1.add_run(f"ОТЧЕТ ПО ПРАКТИЧЕСКОЙ РАБОТЕ № {pz_number}")
    r1.bold = True
    r1.font.size = Pt(16)
    r1.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run(f"Тема: «{pz_title}»")
    r2.bold = True
    r2.font.size = Pt(13)
    r2.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    
    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r3 = p3.add_run(f"Дисциплина: «Веб-разработка» | Проект: «{project_name}»\nСтудент: Храмов | Год: 2026\n")
    r3.font.size = Pt(10)
    r3.font.italic = True
    r3.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    
    return doc

def add_h1(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(12)
    h.paragraph_format.space_after = Pt(4)
    r = h.add_run(text)
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

def add_h2(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(8)
    h.paragraph_format.space_after = Pt(2)
    r = h.add_run(text)
    r.bold = True
    r.font.size = Pt(11.5)
    r.font.color.rgb = RGBColor(0x2B, 0x54, 0x7E)

def add_p(doc, text, bold_prefix=""):
    p = doc.add_paragraph()
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
    p.add_run(text)

def add_bullet(doc, text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
    p.add_run(text)

def add_code(doc, code_str):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    c = t.cell(0, 0)
    set_cell_background(c, "F4F5F7")
    c.width = Inches(6.8)
    p = c.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.0
    r = p.add_run(code_str.strip())
    r.font.name = 'Consolas'
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(0x24, 0x29, 0x2E)
    
    pa = doc.add_paragraph()
    pa.paragraph_format.space_before = Pt(0)
    pa.paragraph_format.space_after = Pt(3)

def save_md(filename, content):
    path = os.path.join(REPORTS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved: {path}")

# ==============================================================================
# ПЗ №2
# ==============================================================================
def generate_pz2():
    doc = create_doc(2, "Сайт университета. Создание базового проекта и приложения", "hogwarts")
    
    add_h1(doc, "1. Цель работы")
    add_p(doc, "Изучение структуры веб-фреймворка Django, освоение команд управления django-admin и manage.py, создание нового проекта, регистрация администратора (суперпользователя), создание и подключение Django-приложения, настройка URL-маршрутизации с использованием include() и RedirectView, а также реализация функции представления index().")
    
    add_h1(doc, "2. Задачи работы")
    add_bullet(doc, "Создать проект Django с названием университета («hogwarts» — Школа Чародейства и Волшебства Хогвартс).", "1. ")
    add_bullet(doc, "Проверить корректность запуска сервера и отображение приветственной страницы фреймворка.", "2. ")
    add_bullet(doc, "Создать учетную запись суперпользователя и протестировать вход в панель администрирования Django (/admin/).", "3. ")
    add_bullet(doc, "Создать приложение для ведения студенческой базы (students).", "4. ")
    add_bullet(doc, "Зарегистрировать приложение в списке INSTALLED_APPS в settings.py.", "5. ")
    add_bullet(doc, "Настроить маршрутизацию в файле hogwarts/urls.py с перенаправлением с корневого URL на адрес приложения через RedirectView.", "6. ")
    add_bullet(doc, "Создать функцию представления index в students/views.py и связать ее с маршрутом в students/urls.py.", "7. ")
    add_bullet(doc, "Проверить отображение стартовой страницы сайта университета.", "8. ")
    
    add_h1(doc, "3. Ход выполнения работы")
    add_h2(doc, "3.1. Создание проекта и приложения")
    add_p(doc, "Для создания проекта и приложения использовались консольные команды Django:")
    add_code(doc, """django-admin startproject hogwarts .
py manage.py migrate
py manage.py createsuperuser --username admin --email admin@hogwarts.edu
py manage.py startapp students""")
    
    add_h2(doc, "3.2. Регистрация приложения в настройках (settings.py)")
    add_code(doc, """INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students',
]""")
    
    add_h2(doc, "3.3. Настройка маршрутизации (urls.py)")
    add_code(doc, """from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('', RedirectView.as_view(url='/students/', permanent=True)),
]""")
    
    add_h2(doc, "3.4. Реализация представления index()")
    add_code(doc, """from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Университет Хогвартс</h1><p>Добро пожаловать в Школу Чародейства и Волшебства!</p>")""")
    
    add_h1(doc, "4. Результаты работы и выводы")
    add_p(doc, "Сервер разработки Django успешно запущен. При переходе по адресу http://127.0.0.1:8000/ происходит автоматический редирект (HTTP 301) на http://127.0.0.1:8000/students/, где отображается название университета. Панель администратора (/admin/) доступна и функционирует.")
    
    doc.save(os.path.join(REPORTS_DIR, "ПЗ_2_Отчет_Сайт_университета_Создание_проекта.docx"))
    
    md_content = """# Отчет по практической работе №2
**Тема:** «Сайт университета. Создание базового проекта и приложения»  
**Проект:** hogwarts  
**Студент:** Храмов  
**Год:** 2026  

## 1. Цель работы
Изучение структуры веб-фреймворка Django, освоение команд управления django-admin и manage.py, создание нового проекта, регистрация администратора (суперпользователя), создание и подключение Django-приложения, настройка URL-маршрутизации с использованием include() и RedirectView, а также реализация функции представления index().

## 2. Задачи работы
1. Создать проект Django с названием университета («hogwarts»).
2. Проверить запуск сервера разработки.
3. Создать аккаунт суперпользователя (createsuperuser) и проверить административную панель.
4. Создать приложение для студенческой базы (students).
5. Добавить приложение в INSTALLED_APPS файла settings.py.
6. Настроить переадресацию с корневого URL на адрес приложения через RedirectView и подключить маршруты через include().
7. Реализовать контроллер index() в views.py и протестировать его вызов.

## 3. Листинги ключевых файлов

### hogwarts/urls.py
```python
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('', RedirectView.as_view(url='/students/', permanent=True)),
]
```

### students/views.py
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Университет Хогвартс</h1><p>Добро пожаловать в Школу Чародейства и Волшебства!</p>")
```

### students/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

## 4. Результаты и выводы
Проект успешно сконфигурирован, работает перенаправление на страницу приложения, панель администратора доступна и готова к работе.
"""
    save_md("ПЗ_2_Отчет_Сайт_университета_Создание_проекта.md", md_content)

# ==============================================================================
# ПЗ №3
# ==============================================================================
def generate_pz3():
    doc = create_doc(3, "Сайт университета. Модели данных и административная панель", "hogwarts")
    
    add_h1(doc, "1. Цель работы")
    add_p(doc, "Освоение объектно-реляционного отображения (ORM) в Django, проектирование схемы базы данных для предметной области университета, описание моделей с различными типами полей (CharField, TextField, DateField, EmailField, ForeignKey), реализация методов __str__() и get_absolute_url(), создание и применение миграций, а также регистрация моделей в Django Admin и наполнение данными.")
    
    add_h1(doc, "2. Задачи работы")
    add_bullet(doc, "Спроектировать структуру сущностей университета Хогвартс: Факультет (Faculty), Учебная группа (Group), Преподаватель (Teacher), Дисциплина (Discipline), Студент (Student).", "1. ")
    add_bullet(doc, "Объявить модели в файле students/models.py с корректными типами полей, ограничениями и параметрами связей on_delete (CASCADE, SET_NULL).", "2. ")
    add_bullet(doc, "Определить метод __str__() для каждой модели для человекопонятного отображения записей в интерфейсе.", "3. ")
    add_bullet(doc, "Реализовать метод get_absolute_url() для формирования ссылки на страницу объекта через reverse().", "4. ")
    add_bullet(doc, "Сформировать и применить миграции к базе данных SQLite (makemigrations, migrate).", "5. ")
    add_bullet(doc, "Зарегистрировать все созданные модели в students/admin.py.", "6. ")
    add_bullet(doc, "Заполнить базу данных через административную панель и скрипт Django ORM (не менее 7 строк для сущностей).", "7. ")
    
    add_h1(doc, "3. Листинг моделей (students/models.py)")
    add_code(doc, """from django.db import models
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
        return f"{self.first_name} {self.last_name}"

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
        return f"{self.first_name} {self.last_name} ({self.group})"

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])""")
    
    add_h1(doc, "4. Настройка admin.py и данные")
    add_code(doc, """from django.contrib import admin
from .models import Faculty, Group, Teacher, Discipline, Student

admin.site.register(Faculty)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Discipline)
admin.site.register(Student)""")
    
    add_p(doc, "База данных заполнена реальными данными Хогвартса:")
    add_bullet(doc, "Факультеты (4 шт.): Гриффиндор, Слизерин, Когтевран, Пуффендуй.", "• ")
    add_bullet(doc, "Группы (4 шт.): ГР-101 (Гриффиндор), СЛ-201 (Слизерин), КГ-301 (Когтевран), ПФ-101 (Пуффендуй).", "• ")
    add_bullet(doc, "Преподаватели (7 чел.): Минерва Макгонагалл, Северус Снегг, Филиус Флитвик, Помона Стебель, Римус Люпин, Рубеус Хагрид, Альбус Дамблдор.", "• ")
    add_bullet(doc, "Дисциплины (7 шт.): Трансфигурация, Зельеварение, Заклинания, Травология, Защита от тёмных искусств, Уход за магическими существами, История магии.", "• ")
    add_bullet(doc, "Студенты (11 чел.): Гарри Поттер, Гермиона Грейнджер, Рон Уизли, Невилл Долгопупс, Драко Малфой, Пэнси Паркинсон, Блейз Забини, Полумна Лавгуд, Чжоу Чанг, Седрик Диггори, Нимфадора Тонкс.", "• ")
    
    add_h1(doc, "5. Заключение")
    add_p(doc, "Модели спроектированы в строгом соответствии с требованиями Django ORM, миграции успешно применены, база данных готова к отображению в интерфейсе.")
    
    doc.save(os.path.join(REPORTS_DIR, "ПЗ_3_Отчет_Сайт_университета_Модели_данных.docx"))
    
    md_content = """# Отчет по практической работе №3
**Тема:** «Сайт университета. Модели данных и административная панель»  
**Проект:** hogwarts  
**Студент:** Храмов  
**Год:** 2026  

## 1. Цель работы
Освоение объектно-реляционного отображения (ORM) в Django, проектирование схемы базы данных для предметной области университета, описание моделей с различными типами полей (CharField, TextField, DateField, EmailField, ForeignKey), реализация методов __str__() и get_absolute_url(), создание и применение миграций, а также регистрация моделей в Django Admin и наполнение данными.

## 2. Разработанные модели (students/models.py)
В системе определены 5 сущностей:
- **Faculty** (Факультет)
- **Group** (Учебная группа)
- **Teacher** (Преподаватель)
- **Discipline** (Учебная дисциплина)
- **Student** (Студент)

Все модели содержат:
1. Корректные параметры типов полей (verbose_name, max_length, on_delete, related_name).
2. Метод __str__() для читаемого строкового представления.
3. Метод get_absolute_url() для генерации канонического URL объекта через reverse().
4. Вложенный класс Meta с русскоязычными именами (verbose_name, verbose_name_plural) и сортировкой (ordering).

## 3. Административная панель и данные
Все модели зарегистрированы в students/admin.py.
В базу данных SQLite внесены данные:
- 4 факультета (Гриффиндор, Слизерин, Когтевран, Пуффендуй)
- 4 учебные группы (ГР-101, СЛ-201, КГ-301, ПФ-101)
- 7 преподавателей (Дамблдор, Макгонагалл, Снегг, Флитвик, Стебель, Люпин, Хагрид)
- 7 дисциплин (Трансфигурация, Зельеварение, Заклинания, Травология, ЗОТИ, Уход за магическими существами, История магии)
- 11 студентов с привязкой к группам и email адресами.

## 4. Выводы
Модели спроектированы в строгом соответствии с требованиями Django ORM, миграции успешно применены, база данных готова к отображению в пользовательском интерфейсе.
"""
    save_md("ПЗ_3_Отчет_Сайт_университета_Модели_данных.md", md_content)

# ==============================================================================
# ПЗ №4
# ==============================================================================
def generate_pz4():
    doc = create_doc(4, "Сайт университета. Шаблоны и отображение данных", "hogwarts")
    
    add_h1(doc, "1. Цель работы")
    add_p(doc, "Освоение механизмов шаблонизации Django Template Engine, проектирование базового шаблона base_generic.html с блоками переопределения ({% block %}), использование механизма наследования ({% extends %}), динамическая передача контекста из функции представления render() в шаблон, отображение статистики объектов из базы данных, а также подключение статических стилей ({% load static %}).")
    
    add_h1(doc, "2. Задачи работы")
    add_bullet(doc, "Создать базовый шаблон base_generic.html, содержащий базовую разметку HTML5, подключение стилей и блоков для заголовка (title), меню (sidebar) и контента (content).", "1. ")
    add_bullet(doc, "Настроить подключение статического CSS-файла static/css/styles.css через тег {% load static %}.", "2. ")
    add_bullet(doc, "Реализовать функцию представления index в students/views.py с агрегацией счетчиков записей через ORM (.count()) и передачей их в шаблон через словарь context.", "3. ")
    add_bullet(doc, "Создать шаблон главной страницы index.html, наследующий base_generic.html и выводящий название университета и количество студентов, преподавателей, групп, факультетов и дисциплин.", "4. ")
    add_bullet(doc, "Организовать боковое меню с возможностью перехода между главной страницей и разделами других сущностей.", "5. ")
    add_bullet(doc, "Создать шаблон-заглушку empty.html для разделов, находящихся в разработке, и настроить для них маршруты в urls.py.", "6. ")
    add_bullet(doc, "Проверить корректность отображения данных из базы данных на веб-странице.", "7. ")
    
    add_h1(doc, "3. Листинги шаблонов и представлений")
    add_h2(doc, "3.1. Представление index() (students/views.py)")
    add_code(doc, """from django.shortcuts import render
from .models import Student, Teacher, Group, Faculty, Discipline

def index(request):
    context = {
        'num_students': Student.objects.count(),
        'num_teachers': Teacher.objects.count(),
        'num_groups': Group.objects.count(),
        'num_faculties': Faculty.objects.count(),
        'num_disciplines': Discipline.objects.count(),
    }
    return render(request, 'index.html', context)""")
    
    add_h2(doc, "3.2. Базовый шаблон (base_generic.html)")
    add_code(doc, """<!doctype html>
<html lang="ru">
  <head>
    {% block title %}<title>Хогвартс</title>{% endblock %}
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
  </head>
  <body>
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-3">
          {% block sidebar %}
            <ul class="sidebar-nav">
              <li><a href="{% url 'index' %}">Главная</a></li>
              <li><a href="{% url 'students_list' %}">Все студенты</a></li>
              <li><a href="{% url 'teachers_list' %}">Все преподаватели</a></li>
              <li><a href="{% url 'groups_list' %}">Все группы</a></li>
              <li><a href="{% url 'faculties_list' %}">Факультеты</a></li>
              <li><a href="{% url 'disciplines_list' %}">Дисциплины</a></li>
            </ul>
          {% endblock %}
        </div>
        <div class="col-sm-9">
          {% block content %}{% endblock %}
        </div>
      </div>
    </div>
  </body>
</html>""")
    
    add_h1(doc, "4. Результаты и выводы")
    add_p(doc, "Система шаблонов Django позволила отделить визуальную разметку от логики обработки запросов. Данные из базы данных SQLite динамически выводятся на главной странице и обновляются автоматически.")
    
    doc.save(os.path.join(REPORTS_DIR, "ПЗ_4_Отчет_Сайт_университета_Шаблоны.docx"))
    
    md_content = """# Отчет по практической работе №4
**Тема:** «Сайт университета. Шаблоны и отображение данных»  
**Проект:** hogwarts  
**Студент:** Храмов  
**Год:** 2026  

## 1. Цель работы
Освоение механизмов шаблонизации Django Template Engine, проектирование базового шаблона base_generic.html с блоками переопределения, использование механизма наследования extends, динамическая передача контекста из функции представления render() в шаблон, отображение статистики объектов из базы данных, а также подключение статических стилей.

## 2. Реализация
1. Базовый шаблон `base_generic.html` определяет общую структуру: меню слева (col-sm-3), основной контент справа (col-sm-9).
2. Подключен статический файл `students/static/css/styles.css`.
3. Представление `index()` передает словарь со счетчиками сущностей (`num_students`, `num_teachers`, `num_groups`, `num_faculties`, `num_disciplines`).
4. Шаблон `index.html` расширяет базовый каркас и выводит актуальные показатели из базы данных.

## 3. Выводы
Применение Django-шаблонов позволило отделить логику обработки запросов от визуального представления данных, обеспечив модульность и масштабируемость веб-приложения.
"""
    save_md("ПЗ_4_Отчет_Сайт_университета_Шаблоны.md", md_content)

# ==============================================================================
# ПЗ №5
# ==============================================================================
def generate_pz5():
    doc = create_doc(5, "Сайт университета. Оформление с использованием Bootstrap", "hogwarts")
    
    add_h1(doc, "1. Цель работы")
    add_p(doc, "Получение практических навыков оформления пользовательского веб-интерфейса с использованием CSS-фреймворка Bootstrap 3, применение классов сетки (Grid System), стилизации навигационных меню (list-group), информационных панелей (panel), кнопок (btn), бейджей (badge), сообщений (alert) и акцентных блоков (jumbotron).")
    
    add_h1(doc, "2. Задачи работы (8 заданий)")
    add_bullet(doc, "Задание 1: Оформить общую сетку страницы (соотношение колонок 3:9 для меню и контента).", "• ")
    add_bullet(doc, "Задание 2: Стилизовать навигационное меню с использованием компонента Bootstrap list-group.", "• ")
    add_bullet(doc, "Задание 3: Оформить заголовок главной страницы компонентом jumbotron.", "• ")
    add_bullet(doc, "Задание 4: Оформить статистику по объектам с помощью информационных карточек panel.", "• ")
    add_bullet(doc, "Задание 5: Разместить информационные блоки в адаптивной сетке row и col-sm-6 / col-sm-4.", "• ")
    add_bullet(doc, "Задание 6: Добавить бейджи (badge) к пунктам навигационного меню для индикации количества объектов.", "• ")
    add_bullet(doc, "Задание 7: Разместить на главной странице интерактивные кнопки btn с различными цветовыми модификаторами (btn-primary, btn-success, btn-warning).", "• ")
    add_bullet(doc, "Задание 8: Добавить информационное сообщение alert-info о состоянии системы.", "• ")
    
    add_h1(doc, "3. Листинг оформленного шаблона index.html")
    add_code(doc, """{% extends "base_generic.html" %}

{% block content %}
  <!-- Jumbotron и Кнопки (Задания 3 и 7) -->
  <div class="jumbotron">
    <h1>Университет Хогвартс</h1>
    <p>Информационная система управления Школой Чародейства и Волшебства.</p>
    <p>
      <a href="{% url 'students_list' %}" class="btn btn-primary btn-lg">Управление студентами</a>
      <a href="{% url 'teachers_list' %}" class="btn btn-success btn-lg">Штат преподавателей</a>
      <a href="{% url 'groups_list' %}" class="btn btn-warning btn-lg">Учебные группы</a>
    </p>
  </div>

  <!-- Информационное оповещение (Задание 8) -->
  <div class="alert alert-info">
    <strong>Справка:</strong> Ниже представлена актуальная статистика по нашей базе данных.
  </div>

  <!-- Адаптивная сетка панелей статистики (Задания 4 и 5) -->
  <div class="row">
    <div class="col-sm-6">
      <div class="panel panel-primary">
        <div class="panel-heading">Студенты</div>
        <div class="panel-body">Зачислено учеников: <strong>{{ num_students }}</strong></div>
      </div>
    </div>
    <div class="col-sm-6">
      <div class="panel panel-success">
        <div class="panel-heading">Преподаватели</div>
        <div class="panel-body">Штат профессоров: <strong>{{ num_teachers }}</strong></div>
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col-sm-4">
      <div class="panel panel-warning">
        <div class="panel-heading">Учебные группы</div>
        <div class="panel-body">Количество: <strong>{{ num_groups }}</strong></div>
      </div>
    </div>
    <div class="col-sm-4">
      <div class="panel panel-danger">
        <div class="panel-heading">Факультеты</div>
        <div class="panel-body">Количество: <strong>{{ num_faculties }}</strong></div>
      </div>
    </div>
    <div class="col-sm-4">
      <div class="panel panel-info">
        <div class="panel-heading">Дисциплины</div>
        <div class="panel-body">Количество: <strong>{{ num_disciplines }}</strong></div>
      </div>
    </div>
  </div>
{% endblock %}""")
    
    add_h1(doc, "4. Результаты и выводы")
    add_p(doc, "Интерфейс веб-приложения приобрел законченный современный дизайн. Все 8 заданий выполнены, компоненты Bootstrap гармонично сочетаются и адаптируются под различные размеры экранов.")
    
    doc.save(os.path.join(REPORTS_DIR, "ПЗ_5_Отчет_Сайт_университета_Bootstrap.docx"))
    
    md_content = """# Отчет по практической работе №5
**Тема:** «Сайт университета. Оформление с использованием Bootstrap»  
**Проект:** hogwarts  
**Студент:** Храмов  
**Год:** 2026  

## 1. Цель работы
Получение практических навыков оформления пользовательского веб-интерфейса с использованием CSS-фреймворка Bootstrap 3, применение классов сетки (Grid System), стилизации навигационных меню (list-group), информационных панелей (panel), кнопок (btn), бейджей (badge), сообщений (alert) и акцентных блоков (jumbotron).

## 2. Выполненные задания
1. **Сетка страницы:** `col-sm-3` для бокового меню и `col-sm-9` для контентной зоны.
2. **Меню навигации:** компонент `list-group` и активный пункт `list-group-item active`.
3. **Заголовок:** блок `jumbotron` с крупным заголовком и подзаголовком.
4. **Панели статистики:** компоненты `panel panel-primary`, `panel-success`, `panel-warning`, `panel-danger`, `panel-info`.
5. **Сетка панелей:** распределение панелей по 2 в ряд (`col-sm-6`) и по 3 в ряд (`col-sm-4`).
6. **Бейджи:** значки `<span class="badge">` внутри элементов меню с актуальным числом объектов.
7. **Кнопки:** кнопки вызова действий `btn btn-primary btn-lg`, `btn-success`, `btn-warning`.
8. **Оповещения:** информационный блок `alert alert-info`.

## 3. Выводы
Применение Bootstrap значительно улучшило пользовательский опыт (UX/UI), сделав навигацию интуитивной, а отображение статистической информации структурированным и наглядным.
"""
    save_md("ПЗ_5_Отчет_Сайт_университета_Bootstrap.md", md_content)

# ==============================================================================
# ПЗ №6
# ==============================================================================
def generate_pz6():
    doc = create_doc(6, "Django: ListView, DetailView и Bootstrap (Приложение Machine / Автопарк)", "iammachines")
    
    add_h1(doc, "1. Цель работы")
    add_p(doc, "Изучение работы представлений на основе классов (Class-Based Views: ListView и DetailView), реализация каталога объектов техники с перечислениями choices (TextChoices), динамическая генерация списочного и подробного представлений, использование Bootstrap 5 для адаптивной верстки (cards, grid, badges), реализация самостоятельных усложнений и ответы на контрольные вопросы.")
    
    add_h1(doc, "2. Задачи работы")
    add_bullet(doc, "Развернуть проект iammachines с приложением catalog.", "1. ")
    add_bullet(doc, "Создать модель Machine со свойствами: название, инвентарный номер, категория (TextChoices), производитель, год выпуска, статус (TextChoices), описание.", "2. ")
    add_bullet(doc, "Применить миграции, зарегистрировать модель в Django Admin и заполнить базу данных минимум 6 объектами техники с разными статусами и категориями.", "3. ")
    add_bullet(doc, "Настроить маршрутизацию в catalog/urls.py для списка техники (machines/) и карточки объекта (machines/<int:pk>/).", "4. ")
    add_bullet(doc, "Создать класс MachineListView(ListView) с переопределением get_queryset() для сортировки по категории и названию.", "5. ")
    add_bullet(doc, "Создать класс MachineDetailView(DetailView) для отображения подробной информации об объекте.", "6. ")
    add_bullet(doc, "Разработать базовый шаблон base.html с подключением Bootstrap 5 через CDN.", "7. ")
    add_bullet(doc, "Создать шаблон списка machine_list.html с адаптивными Bootstrap-карточками, кнопкой «Подробнее», человекочитаемыми choices и блоком {% empty %}.", "8. ")
    add_bullet(doc, "Создать шаблон подробного вида machine_detail.html с описанием характеристик (dl, row), бейджем статуса и кнопкой «Назад к списку».", "9. ")
    add_bullet(doc, "Реализовать минимум 2 самостоятельных усложнения: 1) цветовое кодирование бейджей статуса; 2) вывод общего числа единиц техники над каталогом.", "10. ")
    add_bullet(doc, "Дать подробные и аргументированные ответы на 12 контрольных вопросов.", "11. ")
    
    add_h1(doc, "3. Реализация проекта")
    add_h2(doc, "3.1. Модель Machine (catalog/models.py)")
    add_code(doc, """from django.db import models

class Machine(models.Model):
    class Category(models.TextChoices):
        TRACTOR = 'TR', 'Трактор'
        EXCAVATOR = 'EX', 'Экскаватор'
        CRANE = 'CR', 'Кран'

    class Status(models.TextChoices):
        WORKING = 'W', 'Исправна'
        REPAIR = 'R', 'В ремонте'
        STORAGE = 'S', 'На хранении'
        WRITTEN_OFF = 'D', 'Списана'

    name = models.CharField(max_length=100, verbose_name='Название')
    inventory_number = models.CharField(max_length=50, unique=True, verbose_name='Инвентарный номер')
    category = models.CharField(max_length=2, choices=Category.choices, verbose_name='Категория')
    manufacturer = models.CharField(max_length=100, verbose_name='Производитель')
    year = models.IntegerField(verbose_name='Год выпуска')
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.WORKING, verbose_name='Статус')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name""")
    
    add_h2(doc, "3.2. Представления (catalog/views.py)")
    add_code(doc, """from django.views.generic import ListView, DetailView
from .models import Machine

class MachineListView(ListView):
    model = Machine
    template_name = "catalog/machine_list.html"
    context_object_name = "machines"

    def get_queryset(self):
        return Machine.objects.all().order_by('category', 'name')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_count'] = Machine.objects.count()
        return context

class MachineDetailView(DetailView):
    model = Machine
    template_name = "catalog/machine_detail.html"
    context_object_name = "machine" """)
    
    add_h1(doc, "4. Ответы на контрольные вопросы (ПЗ 6)")
    
    q_and_a_6 = [
        ("1. Чем ListView отличается от DetailView?",
         "ListView предназначен для работы с набором (коллекцией) объектов модели и возвращает список записей (QuerySet), который может быть отсортирован или отфильтрован. DetailView предназначен для работы с ровно одним конкретным объектом модели, извлекаемым из базы данных по его первичному ключу (pk или id) либо слагу (slug)."),
         
        ("2. Зачем у class-based view вызывается метод as_view()?",
         "Диспетчер URL в Django спроектирован для вызова вызываемых объектов-функций (callable), принимающих объект запроса request и возвращающих response. Метод as_view() является фабричным методом класса: он создает и настраивает экземпляр классового представления и возвращает функцию-обертку view(), пригодную для вызова в URLConf."),
         
        ("3. Что задаёт атрибут model?",
         "Атрибут model определяет, к какой модели базы данных привязано данное представление. На основе этого атрибута Django автоматически формирует базовый запрос к базе данных (MyModel.objects.all()), определяет схему данных и генерирует стандартные имена контекста (например, object_list для ListView и object для DetailView)."),
         
        ("4. Для чего используется template_name?",
         "Атрибут template_name явно указывает относительный путь к файлу HTML-шаблона, который должен использоваться для рендеринга страницы. Если его не указать, Django попытается определить шаблон по умолчанию по соглашению (например, <app_name>/<model_name>_list.html)."),
         
        ("5. Что меняет context_object_name?",
         "Атрибут context_object_name переопределяет стандартное системное имя переменной в контексте шаблона. Например, вместо универсального и обезличенного 'object_list' или 'object' он позволяет использовать семантически понятные имена, такие как 'machines' или 'machine'."),
         
        ("6. Откуда DetailView получает pk?",
         "DetailView автоматически извлекает именованный параметр <int:pk> (или <slug>) из словаря именованных аргументов URL-маршрута (kwargs), который парсится диспетчером URL на основе регулярного выражения или конвертера пути из urls.py."),
         
        ("7. Что произойдёт, если объект с таким pk не существует?",
         "DetailView вызовет метод get_object(), который при отсутствии записи в таблице сгенерирует исключение django.http.Http404. Пользователю в браузере будет возвращен стандартный ответ HTTP 404 Not Found («Страница не найдена»), предотвращая сбой сервера с ошибкой 500."),
         
        ("8. Зачем использовать именованные URL вместо жёстко записанных адресов?",
         "Использование именованных маршрутов (через тег {% url 'name' %} или reverse('name')) реализует принцип слабой связанности (DRY). Если в будущем изменится префикс или структура адресов в urls.py, не придется вручную редактировать все HTML-шаблоны и Python-код, так как ссылки перегенерируются автоматически."),
         
        ("9. Для чего в шаблоне используется {% empty %}?",
         "Тег {% empty %} является частью блока {% for %} и выполняется в том случае, когда переданный список объектов пуст или равен None. Это избавляет от необходимости писать внешнюю конструкцию {% if items %}...{% else %} и позволяет вывести дружественное сообщение пользователю (например, «В каталоге пока нет техники»)."),
         
        ("10. Чем {{ machine.status }} отличается от {{ machine.get_status_display }}?",
         "Выражение {{ machine.status }} возвращает «сырое» техническое значение поля из базы данных (например, код 'W' или 'R'). Выражение {{ machine.get_status_display }} вызывает автоматически сгенерированный Django метод модели, который возвращает соответствующее человекочитаемое описание из кортежа choices (например, «Исправна» или «В ремонте»)."),
         
        ("11. Какую задачу решают Bootstrap-классы row и col-*?",
         "Они реализуют 12-колоночную гибкую сетку (Grid System) на основе Flexbox. Класс row создает контейнер-строку с отрицательными отступами, а классы col-* (например, col-12, col-md-6, col-xl-4) задают относительную ширину колонок на разных разрешениях экрана (мобильных, планшетах, десктопах), обеспечивая адаптивность интерфейса."),
         
        ("12. В каком случае имеет смысл переопределять get_queryset()?",
         "Переопределение get_queryset() необходимо, когда требуется изменить логику выборки данных из базы: задать пользовательскую сортировку (как в нашей работе: order_by('category', 'name')), применить сложную фильтрацию по параметрам GET-запроса, ограничить выборку правами текущего пользователя (request.user) или оптимизировать запросы с помощью select_related/prefetch_related.")
    ]
    
    for q, a in q_and_a_6:
        add_p(doc, q, bold_prefix="")
        h_q = doc.paragraphs[-1]
        h_q.runs[0].bold = True
        h_q.runs[0].font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        add_p(doc, a)
    
    add_h1(doc, "5. Заключение")
    add_p(doc, "В рамках практической работы №6 были успешно освоены классовые представления Django ListView и DetailView, работа с перечислениями choices, построение адаптивного двухстраничного каталога на Bootstrap 5, а также реализованы усложнения и даны подробные ответы на теоретические вопросы.")
    
    doc.save(os.path.join(REPORTS_DIR, "ПЗ_6_Отчет_Приложение_Machine_Автопарк.docx"))
    
    md_qa = "\n\n".join([f"### {q}\n{a}" for q, a in q_and_a_6])
    md_content = f"""# Отчет по практической работе №6
**Тема:** «Django: ListView, DetailView и Bootstrap (Приложение Machine / Автопарк)»  
**Проект:** iammachines  
**Студент:** Храмов  
**Год:** 2026  

## 1. Цель работы
Изучение работы представлений на основе классов (Class-Based Views: ListView и DetailView), реализация каталога объектов техники с перечислениями choices (TextChoices), динамическая генерация списочного и подробного представлений, использование Bootstrap 5 для адаптивной верстки (cards, grid, badges), реализация самостоятельных усложнений и ответы на контрольные вопросы.

## 2. Модель Machine и представления
В проекте реализована модель `Machine` со статусами и категориями через `TextChoices`.
- `MachineListView` сортирует объекты по категории и названию через `get_queryset()` и передает общее количество единиц техники через `get_context_data()`.
- `MachineDetailView` обеспечивает просмотр карточки техники с автоматической обработкой 404 при отсутствии ID.

## 3. Самостоятельные усложнения
1. Цветовая дифференциация бейджей статусов (`bg-success` — исправна, `bg-warning` — в ремонте, `bg-secondary` — на хранении, `bg-danger` — списана).
2. Вывод счетчика общего числа единиц техники над каталогом.

## 4. Ответы на контрольные вопросы
{md_qa}

## 5. Выводы
Приложение «Автопарк» полностью функционирует, отвечает всем критериям методических указаний и демонстрирует преимущества использования Generic Class-Based Views в Django.
"""
    save_md("ПЗ_6_Отчет_Приложение_Machine_Автопарк.md", md_content)

# ==============================================================================
# ПЗ №7
# ==============================================================================
def generate_pz7():
    doc = create_doc(7, "Сайт университета: реализация ListView и DetailView", "hogwarts")
    
    add_h1(doc, "1. Цель работы")
    add_p(doc, "Изучение и практическое применение обобщенных представлений на основе классов (Generic Class-Based Views: ListView и DetailView) в рамках проекта «Сайт университета Хогвартс», реализация полного набора маршрутов, контроллеров и шаблонов для всех ключевых сущностей предметной области (Студенты, Преподаватели, Группы, Факультеты, Дисциплины), организация перекрестной навигации между связанными моделями, реализация поиска, пагинации, обработки пустых состояний и подготовка ответов на контрольные вопросы.")
    
    add_h1(doc, "2. Задачи работы")
    add_bullet(doc, "Спроектировать и реализовать пару представлений (ListView и DetailView) для каждой из 5 моделей информационной системы: Student, Teacher, Group, Faculty, Discipline.", "1. ")
    add_bullet(doc, "Определить соответствующие именованные маршруты в students/urls.py (students_list, student_detail, teachers_list, teacher_detail, groups_list, group_detail, faculties_list, faculty_detail, disciplines_list, discipline_detail).", "2. ")
    add_bullet(doc, "Разработать комплекс HTML-шаблонов для спискового отображения (student_list.html, teacher_list.html, group_list.html, faculty_list.html, discipline_list.html) с табличной и карточной версткой, кнопками «Подробнее» и блоками {% empty %}.", "3. ")
    add_bullet(doc, "Разработать шаблоны детальной страницы (student_detail.html, teacher_detail.html, group_detail.html, faculty_detail.html, discipline_detail.html) с хлебными крошками (breadcrumb), полными характеристиками и кнопками возврата к списку.", "4. ")
    add_bullet(doc, "Обеспечить связывание и кликабельность отношений между моделями (на странице группы отображать список ее студентов с переходом в профиль; на странице дисциплины — ссылку на преподавателя; на странице факультета — перечень его групп).", "5. ")
    add_bullet(doc, "Реализовать самостоятельные усложнения: 1) постраничная навигация (пагинация) в StudentListView по 5 записей; 2) форма поиска студентов по фамилии и имени через GET-запрос; 3) вывод счетчиков объектов через бейджи Bootstrap; 4) кликабельные статистические панели на главной странице.", "6. ")
    add_bullet(doc, "Подготовить исчерпывающие ответы на 14 контрольных вопросов.", "7. ")
    
    add_h1(doc, "3. Архитектура и программная реализация")
    add_h2(doc, "3.1. Контроллеры (students/views.py)")
    add_code(doc, """from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Student, Teacher, Group, Faculty, Discipline

def index(request):
    context = {
        'num_students': Student.objects.count(),
        'num_teachers': Teacher.objects.count(),
        'num_groups': Group.objects.count(),
        'num_faculties': Faculty.objects.count(),
        'num_disciplines': Discipline.objects.count(),
    }
    return render(request, 'index.html', context)

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    paginate_by = 5

    def get_queryset(self):
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
    context_object_name = 'discipline'""")
    
    add_h2(doc, "3.2. Маршрутизация (students/urls.py)")
    add_code(doc, """from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('students/', views.StudentListView.as_view(), name='students_list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),

    path('teachers/', views.TeacherListView.as_view(), name='teachers_list'),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),

    path('groups/', views.GroupListView.as_view(), name='groups_list'),
    path('groups/<int:pk>/', views.GroupDetailView.as_view(), name='group_detail'),

    path('faculties/', views.FacultyListView.as_view(), name='faculties_list'),
    path('faculties/<int:pk>/', views.FacultyDetailView.as_view(), name='faculty_detail'),

    path('disciplines/', views.DisciplineListView.as_view(), name='disciplines_list'),
    path('disciplines/<int:pk>/', views.DisciplineDetailView.as_view(), name='discipline_detail'),
]""")
    
    add_h1(doc, "4. Ответы на контрольные вопросы (ПЗ 7)")
    
    q_and_a_7 = [
        ("1. Для чего используется ListView?",
         "ListView предназначен для генерации страниц со списками объектов из базы данных (коллекций записей). Он инкапсулирует логику обращения к ORM, фильтрацию, сортировку, пагинацию (постраничный вывод) и передачу набора объектов в указанный HTML-шаблон под заданным именем."),
         
        ("2. Для чего используется DetailView?",
         "DetailView предназначен для детального отображения одного конкретного объекта модели. Он автоматически извлекает идентификатор (pk или id) из URL, выполняет поиск записи в таблице базы данных и при ее обнаружении передает объект в шаблон. Если запись отсутствует, генерируется стандартный ответ 404 Not Found."),
         
        ("3. Чем ListView отличается от DetailView?",
         "ListView оперирует множеством записей (QuerySet) и формирует списочные представления, поддерживая пагинацию и агрегацию. DetailView оперирует ровно одним экземпляром модели (экземпляром класса Model), привязанным к уникальному идентификатору из пути URL."),
         
        ("4. Что определяет атрибут model?",
         "Атрибут model связывает классовое представление с соответствующим классом модели данных Django. На базе этого атрибута автоматически инициализируется запрос к БД (MyModel.objects.all()), если не переопределен метод get_queryset(), а также формируется базовая метаинформация для контекста."),
         
        ("5. Для чего используется template_name?",
         "template_name позволяет явно задать относительный путь к файлу HTML-шаблона для рендеринга. Это дает возможность использовать собственные имена шаблонов и размещать их в произвольных подкаталогах приложения (например, 'students/student_list.html')."),
         
        ("6. Для чего используется context_object_name?",
         "context_object_name задает имя переменной, под которым извлеченные данные (список объектов или единичный объект) будут доступны внутри шаблона Django. Это делает код шаблона самодокументируемым и читаемым (например, использование 'students' вместо стандартного 'object_list')."),
         
        ("7. Зачем используется as_view()?",
         "Метод as_view() преобразует классовое представление (CBV) в вызываемую функцию представления (FBV). Диспетчер URL Django ожидает именно функцию, принимающую объект HttpRequest и возвращающую HttpResponse. Метод as_view() создает изолированный экземпляр класса на каждый запрос и маршрутизирует вызов к нужному обработчику (get, post и т.д.)."),
         
        ("8. Что означает <int:pk> в маршруте?",
         "Это шаблон динамического сегмента URL с использованием конвертера типов Django. <int:pk> означает, что данный фрагмент пути должен состоять строго из целых неотрицательных чисел и будет передан в представление в виде именованного аргумента pk (primary key — первичный ключ записи)."),
         
        ("9. Как DetailView определяет, какой объект нужно вывести?",
         "DetailView считывает значение аргумента pk (или slug) из параметров маршрута URL, после чего выполняет запрос к QuerySet своей модели вида: model.objects.filter(pk=pk).first(). Метод get_object() возвращает найденный экземпляр модели."),
         
        ("10. Что произойдёт при переходе к несуществующему pk?",
         "Метод get_object() класса DetailView при отсутствии объекта в базе данных вызывает исключение django.http.Http404. Пользователю отдается корректная страница HTTP 404 («Страница не найдена»), а сервер не завершает работу с ошибкой 500."),
         
        ("11. Для чего используется get_queryset()?",
         "Метод get_queryset() переопределяется для динамического управления выборкой записей. Это позволяет реализовать сортировку по определенным полям, фильтрацию по параметрам строки запроса (как поиск по параметру 'q'), разграничение прав доступа и оптимизацию связей (select_related, prefetch_related)."),
         
        ("12. Для чего в шаблоне нужен {% empty %}?",
         "Тег {% empty %} размещается внутри цикла {% for %} и задает блок HTML-разметки, который отображается только в случае, если переданная коллекция пуста. Это исключает необходимость дополнительных проверок {% if %} и позволяет показать сообщение об отсутствии данных (например, «Студенты не найдены»)."),
         
        ("13. Почему лучше использовать {% url %}, а не записывать адрес ссылки вручную?",
         "Использование тега {% url 'имя_маршрута' %} обеспечивает динамическое разрешение адресов (reverse routing). Если шаблон URL в urls.py изменится (например, с /students/ на /university/students/), все ссылки в шаблонах и редиректы в коде обновятся автоматически без необходимости ручной правки."),
         
        ("14. Почему список и подробную информацию целесообразно оформлять отдельными шаблонами?",
         "Список и детальная страница имеют принципиально разное назначение, структуру и требования к верстке. Список должен быть компактным, табличным или карточным, оптимизированным для быстрого обзора и фильтрации множества элементов. Детальная карточка содержит расширенный состав атрибутов, связанных таблиц и элементов управления. Разделение шаблонов повышает модульность, удобство сопровождения и производительность рендеринга.")
    ]
    
    for q, a in q_and_a_7:
        add_p(doc, q, bold_prefix="")
        h_q = doc.paragraphs[-1]
        h_q.runs[0].bold = True
        h_q.runs[0].font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        add_p(doc, a)
    
    add_h1(doc, "5. Заключение")
    add_p(doc, "В рамках практической работы №7 информационная система «Университет Хогвартс» была полностью модернизирована с использованием Generic Class-Based Views (ListView и DetailView). Реализованы списочные и детальные страницы для всех пяти сущностей системы, перекрестная навигация, поиск, пагинация и стилизация на базе Bootstrap. Подготовлены развернутые ответы на все 14 контрольных вопросов.")
    
    doc.save(os.path.join(REPORTS_DIR, "ПЗ_7_Отчет_Сайт_университета_ListView_DetailView.docx"))
    
    md_qa7 = "\n\n".join([f"### {q}\n{a}" for q, a in q_and_a_7])
    md_content = f"""# Отчет по практической работе №7
**Тема:** «Сайт университета: реализация ListView и DetailView»  
**Проект:** hogwarts  
**Студент:** Храмов  
**Год:** 2026  

## 1. Цель работы
Изучение и практическое применение обобщенных представлений на основе классов (Generic Class-Based Views: ListView и DetailView) в рамках проекта «Сайт университета Хогвартс», реализация полного набора маршрутов, контроллеров и шаблонов для всех ключевых сущностей предметной области (Студенты, Преподаватели, Группы, Факультеты, Дисциплины), организация перекрестной навигации между связанными моделями, реализация поиска, пагинации, обработки пустых состояний и подготовка ответов на контрольные вопросы.

## 2. Реализация архитектуры CBV
Для всех пяти моделей созданы пары ListView и DetailView:
- StudentListView (с пагинацией и поиском через get_queryset) и StudentDetailView.
- TeacherListView и TeacherDetailView (с выводом списка читаемых дисциплин).
- GroupListView и GroupDetailView (с выводом всех студентов группы со ссылками).
- FacultyListView и FacultyDetailView (с выводом всех групп факультета).
- DisciplineListView и DisciplineDetailView (со ссылкой на карточку преподавателя).

## 3. Самостоятельные усложнения
1. Постраничная навигация в списке студентов (paginate_by = 5).
2. Полнотекстовый поиск по фамилии и имени студента через GET-параметр q.
3. Кликабельные связанные сущности во всех детальных представлениях.
4. Контекстный процессор для актуализации бейджей количества объектов во всех шаблонах.
5. Интерактивная главная страница с переходом во все разделы из информационных панелей.

## 4. Ответы на контрольные вопросы
{md_qa7}

## 5. Выводы
Применение ListView и DetailView позволило сократить объем шаблонного кода, стандартизировать обработку типичных сценариев (списки, карточки, 404, пагинация) и построить масштабируемую веб-систему университета.
"""
    save_md("ПЗ_7_Отчет_Сайт_университета_ListView_DetailView.md", md_content)

if __name__ == "__main__":
    print("Генерация отчетов...")
    generate_pz2()
    generate_pz3()
    generate_pz4()
    generate_pz5()
    generate_pz6()
    generate_pz7()
    print("Все отчеты успешно сгенерированы в папку 'reports/'!")
