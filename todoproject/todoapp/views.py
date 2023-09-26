from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Task

# Create your views here.

def home(request):

    task_op=Task.objects.all()


    if request.method=="POST":
        name=request.POST.get('task')
        priority = request.POST.get('priority')
        date=request.POST.get('date')
        task=Task(name=name,priority=priority,date=date)
        task.save()

    return render(request,"home.html",{'task':task_op})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,taskid):
    task=Task.objects.get(id=taskid)
    form=TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'task':task})
