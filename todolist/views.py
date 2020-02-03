from django.shortcuts import render, redirect
from .models import Todo


# Create your views here.
def home(request):

	if request.method == "POST":
		if request.POST.get('addTodo') == '':
			content = {'警告': '待办事项不能为空！', 'listTodo': Todo.objects.all()}
			return render(request, 'todolist/home.html', content)
		else:
			a_row = Todo(name=request.POST.get('addTodo'))
			a_row.save()
			content = {'listTodo': Todo.objects.all()}
			return render(request, 'todolist/home.html', content)
	else:
		content = {'listTodo': Todo.objects.all()}
		return render(request, 'todolist/home.html', content)

def delete(request, item_id):
	a_row = Todo.objects.get(id=item_id)
	a_row.delete()
	return redirect('todolist:主页')

def finish(request, item_id):

	a_row = Todo.objects.get(id=item_id)
	a_row.done = True
	a_row.save()
	return redirect('todolist:主页')

def unfinish(request, item_id):

	a_row = Todo.objects.get(id=item_id)
	a_row.done = False
	a_row.save()
	return redirect('todolist:主页')

def about(request):
	return render(request, 'todolist/about.html')

def edit(request, item_id):

	if request.method == "POST":
		if request.POST.get('editedTodo') == '':
			content = {'警告': '待办事项不能为空！'}
			return render(request, 'todolist/edit.html', content)
		else:
			a_row = Todo.objects.get(id=item_id)
			a_row.name = request.POST.get('editedTodo')
			a_row.save()
			content = {'listTodo': Todo.objects.all()}
			return redirect('todolist:主页')
	else:
		content = {'forEditTodo': Todo.objects.get(id=item_id).name}
		return render(request, 'todolist/edit.html', content)
