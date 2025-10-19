from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Todo
from .forms import TodoForm, UpdateUserForm, UpdateTaskForm
from django.contrib.auth.models import User

# Create your views here.


@login_required
def home(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("home")

    tasks = Todo.objects.filter(user=request.user)
    return render(request, "todo/home.html", {"form": form, "tasks": tasks})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id, user=request.user)
    if request.method == 'GET':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
    return redirect("home")


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id, user=request.user)
    task.complete = not task.complete
    task.save()
    return redirect("home")


@login_required
def settings_page(request):
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect("settings_page")
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request, "todo/settings.html", {"form": form})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id, user=request.user)
    
    if request.method == "POST":
        form = UpdateTaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect("home")
    else:
        form = UpdateTaskForm(instance=task)
    
    return render(request, 'todo/edit_task.html', {"form": form, "task": task})