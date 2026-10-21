from django.views.generic import ListView, DetailView
from .models import Machine

class MachineListView(ListView):
    model = Machine
    template_name = "catalog/machine_list.html"
    context_object_name = "machines"

    def get_queryset(self):
        # Сортировка по категории, затем по названию
        return Machine.objects.all().order_by('category', 'name')
    
    def get_context_data(self, **kwargs):
        # Усложнение: передаем общее количество объектов в шаблон
        context = super().get_context_data(**kwargs)
        context['total_count'] = Machine.objects.count()
        return context

class MachineDetailView(DetailView):
    model = Machine
    template_name = "catalog/machine_detail.html"
    context_object_name = "machine"