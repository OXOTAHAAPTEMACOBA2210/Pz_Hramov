from django.urls import path
from .views import MachineListView, MachineDetailView

urlpatterns = [
    path("machines/", MachineListView.as_view(), name="machine_list"),
    path("machines/<int:pk>/", MachineDetailView.as_view(), name="machine_detail"),
]