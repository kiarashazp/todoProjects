from .models import Todo
from .forms import CreateTodoForm, UpdateTodoForm, SearchTodoForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(LoginRequiredMixin, View):
    form_class = SearchTodoForm

    def get(self, request):
        all_todo = Todo.objects.filter(user=request.user)
        if search := request.GET.get('search'):
            all_todo = all_todo.filter(title__icontains=request.GET['search'])
        return render(request, 'home/home.html', {'todos': all_todo, 'form': self.form_class, 'search': search})


class DeleteTask(LoginRequiredMixin, View):
    def get(self, request, todo_id):
        Todo.objects.get(pk=todo_id).delete()
        messages.success(request, 'delete successfully', 'success')
        return redirect('home:home')


class CreateTask(LoginRequiredMixin, View):
    form_class = CreateTodoForm

    def get(self, request):
        form = self.form_class
        return render(request, 'home/create.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'create successfully', 'success')
            return redirect('home:detail_task', new_form.id)
        messages.success(request, 'create unsuccessfully', 'warning')
        return redirect('home:create_task')


class UpdateTask(LoginRequiredMixin, View):
    form_class = UpdateTodoForm

    def setup(self, request, *args, **kwargs):
        self.task = get_object_or_404(Todo, pk=kwargs['todo_id'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        todo = self.task
        if not todo.user.id == request.user.id:
            messages.error(request, 'you cant update this post', 'danger')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        todo = self.task
        form = self.form_class(instance=todo)
        return render(request, 'home/update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        todo = self.task
        form = self.form_class(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'your todo updated successfully', 'success')
            return redirect('home:detail_task', todo.id)
        messages.success(request, 'update unsuccessfully', 'warning')
        return redirect(todo.get_absolute_url_update())


class DetailTask(LoginRequiredMixin, View):
    def get(self, request, todo_id):
        todo = Todo.objects.get(pk=todo_id)
        return render(request, 'home/detail.html', {'todo': todo})
