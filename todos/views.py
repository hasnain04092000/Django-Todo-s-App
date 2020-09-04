from django.shortcuts import render, redirect
from .forms import TaskForms
from .models import Task
# Create your views here.


def index(request):
    tasks = Task.objects.all()

    form = TaskForms()
    if request.method == 'POST':
        form = TaskForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'index.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    
    form = TaskForms(instance=task)

    if request.method == 'POST':
        form = TaskForms(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'update.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'delete.html', context)