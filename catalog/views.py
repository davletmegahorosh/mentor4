from django.shortcuts import render, redirect
from .models import Pizza, Comments_pizza
from catalog.forms import PizzaCreateForm, CommentCreate

PAGINATION_LIMIT = 4

def main(request):
    if request.method == 'GET':
        context = {'page_name' : 'home'}
        return render(request, 'layouts/index.html', context=context)

def pizza_view(request):
    if request.method =='GET':
        pizza = Pizza.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page')) if request.GET.get('page') is not None else 1
        if search is not None:
            pizza = Pizza.objects.filter(
                name__icontains=search
            )
        max_page = pizza.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page=round(max_page) +1

        if max_page < 1:
            max_page = 0

        pizza = pizza[PAGINATION_LIMIT*(page-1):PAGINATION_LIMIT*page]

        context = {
            'products' : pizza,
            'user' : request.user,
            'max_page' : range(1, round(max_page)+1)
        }
        return render(request, 'catalog/catalog.html', context=context)

def pizza_detail_view(request, id):
    if request.method == 'GET':
        pizza = Pizza.objects.get(id=id)
        comments = Comments_pizza.objects.filter(pizza=pizza)
        context = {
            'product': pizza,
            'comments': comments,
            'form': CommentCreate(),
        }
        return render(request, 'catalog/detail.html', context=context)
    if request.method == 'POST':
        form = CommentCreate(data=request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                Comments_pizza.objects.create(
                    author=request.user,
                    text=form.cleaned_data.get('text'),
                    pizza=Pizza.objects.get(id=id)
                )
                return redirect(request.path)
            else:
                form.add_error(None, 'Вы не авторизованы для добавления комментария.')
        pizza = Pizza.objects.get(id=id)
        comments = Comments_pizza.objects.filter(pizza=pizza)
        context = {
            'product': pizza,
            'comments': comments,
            'form': form,
        }
        return render(request, 'catalog/detail.html', context=context)



def create_pizza(request):
    if request.method == 'GET' and not request.user.is_anonymous:
        context={
            'form' : PizzaCreateForm
        }
        return render(request, 'catalog/create.html', context=context)
    elif request.user.is_anonymous:
        return redirect('/pizza')
    if request.method == 'POST':
        form = PizzaCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Pizza.objects.create(
                author = request.user,
                image = form.cleaned_data.get('image'),
                name = form.cleaned_data.get('name'),
                price = form.cleaned_data.get('price')
            )
            return redirect('/pizza/')
        return render(request, 'catalog/create.html', context={
            'form' : form
        })