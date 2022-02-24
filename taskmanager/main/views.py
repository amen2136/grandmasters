
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import News, Todo
from .forms import NewsForm, TodoForm

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error=' '
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_s')
        else:
            error = 'form is incorrect'

    form = NewsForm()    
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

def news(request):
    newsmd = News.objects.order_by('-id')
    return render(request, 'main/news.html', {'title': 'main news of the site', 'news' : newsmd})

def todolist(request):
    error=' '
    item_list = Todo.objects.order_by("-date")
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
        else:
            error = 'form is incorrect'

    form = TodoForm()    
    page = {
        "forms" : form,
        "list" : item_list,
        "title" : "TODOLIST",
    }
    # tasks = Task.objects.all()
    return render(request, 'main/todolist.html', page)

# def remove(request, item_id):
#     item = Todo.objects.get(id = item_id)
#     item.delete()
#     messages.info(request, "item removed !!!")

#     return render('todo')


# def todoappView(request):
#     all_todo_items = todolistItem.objects.all()
#     return render(request, 'main/todolist.html',
#     {'all_items' : all_todo_items,'title' : 'my to do listttt'})

# def addTodoView(request):
#     x = request.POST['content']
#     new_item = todolistItem(context = x)
#     new_item.save()
#     return HttpResponseRedirect('/todoapp/')
