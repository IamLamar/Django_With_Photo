from django.shortcuts import render,redirect
from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request,'task_list.html',{'task':tasks})

def add_task(request):
    if request.method == 'POST':#если метод запроса пост
        form = TaskForm(request.POST)# у нас создается функция с методом пост для заполнения
        if form.is_valid():#если данные заполнены введены корректно они добавляются в бд
            return redirect('task_list')
    else:
        form = TaskForm()#иначе нас ожидает форма для принятия данных 
    return render(request,'add_task.html',{'form':form})#в визуале пустая форма в html шаблоне

# Create your views here.
