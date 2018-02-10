from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.models import User
from django import forms
from django.views.generic import View
from django.contrib.auth import authenticate,login

class index(generic.TemplateView):
    template_name = 'login/index_temp.html'

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserFormView(View):
    form_class=UserForm
    template_name='login/registration_temp.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form =self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            if user is not None:
                return render(request,'login/login_temp.html',{'register':True})


        return  render(request,self.template_name,{'form':form})

def verify(request):
    if request.method == "POST":
        uname = request.POST.get('uname', default=None)
        pas = request.POST.get('pass')
        user = authenticate(username=uname, password=pas)

        if user is not None:
            if user.is_active:
                login(request, user)

            return redirect('register:index')

    return render(request, 'login/login_temp.html',{'error_message':True})


class login(generic.TemplateView):
    template_name = 'login/login_temp.html'

def register(request):
    return render(request, 'login/registration_temp.html', {'error_message': ''})

