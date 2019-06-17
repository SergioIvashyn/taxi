from django.shortcuts import render

from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View,ListView
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView

from .models import *
from .forms import *
from .utils import *

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
    order = ''
    if hasattr(request.user.myuser,'client'):
        order = Order.objects.filter(client=request.user.myuser.client)
    if hasattr(request.user.myuser,'driver'):
        order = Order.objects.filter(driver=request.user.myuser.driver)    
    return render(request, 'taxi/profile.html',context={
        'order':order,
        })


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'taxi/user_sign_in_form.html')
    else:
        phone = request.POST.get('username', False)
        password = request.POST.get('password', False)
        try:
            username = MyUser.objects.get(phonenumber=phone)
        except Exception as e:
            return render(request, 'taxi/user_sign_in_form.html')
        
        username = MyUser.objects.get(phonenumber=phone)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'taxi/user_sign_in_form.html')

#crud Order

def order_list(request):
    if Order.objects.filter(driver=request.user.myuser.driver).exists():
        return redirect('profile')
    order = Order.objects.filter(driver__isnull=True)
    return render(request,'taxi/list_order.html',context={'order':order})

def order_operator_list(request):
    order = Order.objects.all()
    return render(request,'taxi/list_order_operator.html',context={'order':order})


class OrderCreateOpertor(LoginRequiredMixin,ObjectCreateMixin, View):
    model_form = OrderFormOperator
    model = Order
    template = 'taxi/create_order_operator.html'
    raise_exception = True

    def get(self,request):
        form = self.model_form()
        return render(request, self.template,context={'form':form})

    def post(self,request):
        bound_form = self.model_form(request.POST or None,request.FILES or None)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect('order_operator_list')
        return render(request,self.template,context={'form':bound_form})




class OrderCreate(LoginRequiredMixin,ObjectCreateMixin, View):
    model_form = OrderForm
    model = Order
    template = 'taxi/create_order.html'
    raise_exception = True

    def get(self,request):
        form = self.model_form()
        return render(request, self.template,context={'form':form})

    def post(self,request):
        bound_form = self.model_form(request.POST or None,request.FILES or None)
        if bound_form.is_valid() and not Order.objects.filter(client=request.user.myuser.client,status_id=1).exists():
            new_obj = bound_form
            order = Order.objects.create(
                client = request.user.myuser.client,
                place_to=new_obj.cleaned_data['place_to'],
                place_from=new_obj.cleaned_data['place_from'],
                status_id=1
                ).save()   
            return redirect('profile')
        return render(request,self.template,context={'form':bound_form})


class OrderUpdate(LoginRequiredMixin,ObjectUpdateMixin,View):
    model = Order
    model_form = OrderFormDriver
    template = 'taxi/update.html'
    raise_exception = True
    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request,self.template,context={'form':bound_form,'obj':obj})

    def post(self,request,slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST or None,request.FILES or None,instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect('profile')
        return render(request,self.template,context={'form':bound_form,'obj':obj})


class OrderDelete(LoginRequiredMixin,ObjectDeleteMixin,View):
    model = Order
    template = 'taxi/delete.html'
    redirect_url = 'profile'
    raise_exception = True


def order_driver(request):
    order = get_object_or_404(Order,id=request.POST.get('id'))
    order.driver=request.user.myuser.driver
    order.status_id=2
    order.save()
    return redirect('profile')


#CRUD driver

class DriverUpdate(LoginRequiredMixin,ObjectUpdateMixin,View):
    model = Driver
    model_form = DriverForm
    template = 'taxi/update.html'
    raise_exception = True

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request,self.template,context={'form':bound_form,'obj':obj})

    def post(self,request,slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST or None,request.FILES or None,instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect('profile')
        return render(request,self.template,context={'form':bound_form,'obj':obj})


class OrderUpdateOperator(LoginRequiredMixin,ObjectUpdateMixin,View):
    model = Order
    model_form = OrderFormDriver
    template = 'taxi/update.html'
    raise_exception = True
    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request,self.template,context={'form':bound_form,'obj':obj})

    def post(self,request,slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST or None,request.FILES or None,instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect('profile')
        return render(request,self.template,context={'form':bound_form,'obj':obj})

