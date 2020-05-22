from django.shortcuts import render,redirect

# Create your views here.

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout

def signup(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             #  log the user in
             login(request, user)
             return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def login_view(request):

	#return HttpResponse("About Page")
    #articles = Article.objects.all().order_by('date')
    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
               return redirect('articles:list')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', { 'form': form })


def logout_view(request):
	#return HttpResponse("About Page")
    #articles = Article.objects.all().order_by('date')
    if request.method == 'POST':
        logout(request)

        return redirect('articles:list')
