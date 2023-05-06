from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoForm

# Create your views here.


def home(request):
    list_of_items = Todo.objects.order_by('-date')
    if request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    form = TodoForm()

    context = {"forms": form, "list_of_items": list_of_items,
               "title": "TODO LIST"}

    return render(request, 'todo/index.html', context=context)


def delete(request, id):
    item = Todo.objects.get(id=id)
    item.delete()
    messages.info(request=request, message="Item deleted successfully")
    return redirect(to="homepage")
