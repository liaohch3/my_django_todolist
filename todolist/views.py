from django.shortcuts import render, redirect

lst = [
	{'待办事项': '遛狗', '完成情况': False},
	{'待办事项': '拖地', '完成情况': False},
	{'待办事项': '拖地', '完成情况': True},
	{'待办事项': '拖地', '完成情况': False},
]

# Create your views here.
def home(request):
	global lst

	if request.method == "POST":
		if request.POST.get('添加的待办事项') == '':
			content = {'警告': '待办事项不能为空！', '清单': lst}
			return render(request, 'todolist/home.html', content)
		else:
			lst.append({'待办事项': request.POST.get('添加的待办事项'), '完成情况': False})
			content = {'清单': lst}
			return render(request, 'todolist/home.html', content)
	else:
		content = {'清单': lst}
		return render(request, 'todolist/home.html', content)

def delete(request, forloop_counter):
	global lst

	lst.pop(int(forloop_counter) - 1)
	return redirect('todolist:主页')

def finish(request, forloop_counter):
	global lst

	lst[int(forloop_counter) - 1]['完成情况'] = True
	return redirect('todolist:主页')

def unfinish(request, forloop_counter):
	global lst

	lst[int(forloop_counter) - 1]['完成情况'] = False
	return redirect('todolist:主页')

def about(request):
	return render(request, 'todolist/about.html')

def edit(request, forloop_counter):
	global lst

	if request.method == "POST":
		if request.POST.get('编辑后的待办事项') == '':
			content = {'警告': '待办事项不能为空！'}
			return render(request, 'todolist/edit.html', content)
		else:
			# lst.append({'待办事项': request.POST.get('编辑后的待办事项'), '完成情况': False})
			lst[int(forloop_counter)-1]['待办事项'] = request.POST.get('编辑后的待办事项')
			content = {'清单': lst}
			return redirect('todolist:主页')
	else:
		content = {'待修改事项': lst[int(forloop_counter)-1]['待办事项']}
		return render(request, 'todolist/edit.html', content)
