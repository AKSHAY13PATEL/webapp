from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import View, FormView
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import Document,RepoData
from .forms import DocumentForm,UserForm,RepoForm
import os
from git import Repo

def index(request):
    repo_list = RepoData.objects.all()
    return render(request, 'login/index_temp.html', {'repo_list': repo_list})

def RepoFormView(request):

    if request.method == 'POST':
        form = RepoForm(request.POST)
        if form.is_valid():
            dirname = form.cleaned_data['repo_name']
            os.mkdir(os.path.join('media\documents', dirname))

            repo_dir = os.path.join("C:\\Users\\Akshay Patel\\Desktop\\webapp\\media\\documents\\", dirname )
            file_name = os.path.join(repo_dir, 'new-file')
            r = Repo.init(repo_dir)

            open(file_name, 'wb').close()
            r.index.add([file_name])
            r.index.commit("initial commit")


            form.save()

            return redirect('reg:index')

        else:
            return render(request,'login/index_temp.html',{'msg':"Repository has not been created"})
    else:
        form =RepoForm()
        return render(request, 'login/repo_temp.html', {'form':form})


def RepoDetail(request,name_repo):

    if request.method == 'GET':
        documents = Document.objects.all()
        repo = Repo("C:\\Users\\Akshay Patel\\Desktop\\webapp\\media\\documents\\"+ name_repo)
        assert not repo.bare
        assert not repo.is_dirty()
        untracked_list = repo.untracked_files
        return render(request,'login/repo_detail_temp.html',{'documents' : documents, 'name_repo' : name_repo , 'untracked_list' : untracked_list})
    else:
        documents = Document.objects.all()
        repo = Repo("C:\\Users\\Akshay Patel\\Desktop\\webapp\\media\\documents\\"+ name_repo)
        assert not repo.bare
        assert not repo.is_dirty()
        untracked_list = repo.untracked_files
        for file in untracked_list:
            repo.index.add([file])
            repo.index.commit("This is commit for file :" + file)

        assert not repo.is_dirty()
        untracked_list = repo.untracked_files
        return render(request,'login/repo_detail_temp.html', {'untracked_list' : untracked_list , 'documents' : documents , 'name_repo' : name_repo})





def model_form_upload(request,name_repo):


    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('reg:index')
    else:
        form = DocumentForm()
    return render(request, 'login/model_form_upload.html', {
        'form': form , 'name_repo' : name_repo
    })

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
                return render(request,'login/login_temp.html',{'reg':True})


        return  render(request,self.template_name,{'form':form})

def verify(request):
    if request.method == "POST":
        uname = request.POST.get('uname', default=None)
        pas = request.POST.get('pass')
        user = authenticate(username=uname, password=pas)

        if user is not None:
            if user.is_active:
                auth_login(request,user)
                return redirect('reg:index')



    return render(request, 'login/login_temp.html',{'error_message':True})


class login(generic.TemplateView):
    template_name = 'login/login_temp.html'

def register(request):
    return render(request, 'login/registration_temp.html', {'error_message': ''})


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'login/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'login/simple_upload.html')

