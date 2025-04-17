from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category
from .forms import CategoryForm

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category:category_list')
    else:
        form = CategoryForm()
    return render(request, 'category/create.html', {'form': form})

@login_required
def category_update(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/update.html', {'form': form, 'category': category})

@login_required
def category_delete(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        category.delete()
        return redirect('category:category_list')
    return render(request, 'category/delete.html', {'category': category})