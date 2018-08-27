from django.shortcuts import render

from todolist.models import todo

# Create your views here.
def index(request):

	items = todo.objects.all()

	return render(request, "index.html", {"items" : items })
