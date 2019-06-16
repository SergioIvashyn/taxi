from django.shortcuts import render

from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView


from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView

from .models import *
from .forms import *


# Create your views here.
def index(request):
	return render(request,'taxi/index.html')


#auth

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'taxi/register.html', {'form': form})




def profile(request):
    return render(request, 'taxi/profile.html')
