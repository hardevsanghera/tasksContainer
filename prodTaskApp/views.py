from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from prodTaskApp.models import Task
from django.urls import reverse_lazy

# Create your views here.
class TaskListView(ListView):
    model = Task
    #default template_name is task_list.html
    #default context_object_name is task_list

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')

class TaskCreateView(CreateView):
    model = Task
    fields = ('name',)
    success_url = reverse_lazy('tasks')