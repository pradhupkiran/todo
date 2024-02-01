from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.


def home(request):
    list_todo = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'home.html', {'list_todo': list_todo})


def delete(request, id):
    del_todo = Task.objects.get(id=id)
    if request.method == 'POST':
        del_todo.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request,id):
    update_todo=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=update_todo)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'update_todo':update_todo})


class Tasklistview(ListView):
    model=Task
    template_name='home.html'
    context_object_name='list_todo'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'classupdate.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('Taskdetailview',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('classhome')