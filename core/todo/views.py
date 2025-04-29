from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from todo.forms import TodoForm
# Create your views here.
def todoView(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            form = TodoForm()
    todos = request.user.todo_set.all()
    context = {
        'form': form,
        'todos': todos
    }
    return render(request, 'todo/todo.html', context) 

def deleteTodo(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    todo = request.user.todo_set.get(id=pk)
    todo.delete()
    return redirect('todo:todo-view')

@login_required
def updateTodo(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    todo = get_object_or_404(Todo, id=pk)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:todo-view')
    return render(request, 'todo/update.html', {'todo': todo})    