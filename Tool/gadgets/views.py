from django.shortcuts import render
from . import models
from .forms import ToDoForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
import json

def home(request):
    return render(request, "gadgets/home.html")

def about(request):
    return render(request, "gadgets/about.html")

@login_required(login_url='/accounts/google/login/')
def todo(request):
    form = ToDoForm()
    current_user=request.user
    if request.method == 'POST' and request.is_ajax():
        form = ToDoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            content = request.POST['content']
            print(content)
            instance.save()
            pk = instance.pk
            time = timezone.localtime(timezone.now())
            return JsonResponse({'success':True, 'content':content, 'pk':pk, 'time':time}, status=200)

    context = {
        'todos': models.ToDo.objects.all().filter(author=current_user.id),
        'form': form,
    }
    return render(request, "gadgets/todo.html", context)

@login_required
def todo_delete(request, pk):
    current_user=request.user
    test = models.ToDo.objects.filter(pk=pk).first()
    if test.author == current_user:
        todo = get_object_or_404(models.ToDo, pk=pk)  # Get your current cat
        if request.method == 'POST':         # If method is POST,
            todo.delete()                     # delete the cat.
            return redirect('/todo')             # Finally, redirect to the homepage.

        return render(request, 'todo.html', {'todo': todo})
    else:
        return redirect('/todo')
