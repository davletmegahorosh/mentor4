from django.shortcuts import render, redirect
from .models import Pizza, Comments_pizza
from catalog.forms import PizzaCreateForm, CommentCreate

def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def pizza_view(request):
    if request.method =='GET':
        pizza = Pizza.objects.all()
        context = {
            'products' : pizza
        }
        return render(request, 'catalog/catalog.html', context=context)

def pizza_detail_view(request, id):
    if request.method =='GET':
        pizza = Pizza.objects.get(id=id)
        comments = Comments_pizza.objects.filter(pizza=pizza)
        context = {
            'product' : pizza,
            'comments' : comments,
            'form' : CommentCreate,
        }
        return render(request, 'catalog/detail.html', context=context)
    if request.method == 'POST':
        form = CommentCreate(data=request.POST)
        if form.is_valid():
            Comments_pizza.objects.create(
                text = form.cleaned_data.get('text'),
                pizza = Pizza.objects.get(id=id)
            )
            return redirect(request.path)
        return render(request, 'catalog/create.html', context={
            'form': form
        })


def create_pizza(request):
    if request.method == 'GET':
        context={
            'form' : PizzaCreateForm
        }
        return render(request, 'catalog/create.html', context=context)
    if request.method == 'POST':
        form = PizzaCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Pizza.objects.create(
                image = form.cleaned_data.get('image'),
                name = form.cleaned_data.get('name'),
                price = form.cleaned_data.get('price')
            )
            return redirect('/pizza/')
        return render(request, 'catalog/create.html', context={
            'form' : form
        })