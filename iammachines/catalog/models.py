from django.db import models

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
        return self.name