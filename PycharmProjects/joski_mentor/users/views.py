from django.shortcuts import render, redirect
from users.forms import AuthForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def auth_view(request):
    if request.method == 'GET':
        context = {
            'form' : AuthForm
        }
        return render(request, 'users/auth.html', context=context)
    if request.method == 'POST':
        data = request.POST
        form = AuthForm(data=data)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )
            if user:
                login(request, user)
                return redirect('/')

            else:
                form.add_error('usernsme', 'ошибка')
        return render(request, 'users/auth.html', context={
            'form' : form
        })