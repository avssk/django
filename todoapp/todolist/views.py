from django.shortcuts import render, redirect

from todolist.models import todo
from todolist.forms import addtodo

# Create your views here.
def index(request):

	items = todo.objects.all()

	return render(request, "index.html", {"items" : items })


def addtask(request):
	my_form = addtodo()
	if request.method == "POST":
		my_form = addtodo(request.POST)
		if my_form.is_valid():
			todo.objects.create(**my_form.cleaned_data)
		
		return redirect("http://127.0.0.1:8000") # redirects to the todo page

	return render(request, "addtask.html", {"form": my_form })
	

