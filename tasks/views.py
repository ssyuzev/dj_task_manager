from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect


from .forms import NewTaskForm
from .models import Task
from .helpers import get_categories


@login_required()
def task_list(request):
    me = request.user
    categories = get_categories()
    tasks = Task.objects.filter(Q(author=me) | Q(performers=me)).distinct()
    category = request.POST.get('category', 'all')
    types = request.POST.get('types', 'all')
    if request.method == 'POST':
        if category != 'all':
            tasks = tasks.filter(category=category)
        if 'author' in types:
            tasks = tasks.filter(author=me)
        if 'performer' in types:
            tasks = tasks.filter(performers=me)
        print(category)
    return render(
        request,
        'home.html',
        {
            'categories': categories,
            'category': category,
            'tasks': tasks,
            'types': types,
        }
    )


@login_required()
def new_task(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            form.save_m2m()
            print(request.POST)
            return redirect('home')
    else:
        form = NewTaskForm()
    return render(request, 'new_task.html', {'form': form})


@login_required()
def check_task_title(request):
    if request.is_ajax():
        if request.method == 'GET':
            q = request.GET.get('search_text', None)
            q = q.strip()
            print(q)
            if q:
                data = {
                    'is_exist': Task.objects.filter(
                        title__istartswith=q).exists()
                }
            else:
                data = {
                    'is_exist': False
                }
            return JsonResponse(data)
