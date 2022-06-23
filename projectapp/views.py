from django.shortcuts import render,redirect,get_object_or_404
from .forms import BlogModelForm
from .models import Blog
# Create your views here.

def home(request):
    post=Blog.objects.all()
    return render(request,'index.html',{'post':post})
    
def modelformcreate(request):
    if request.method=="POST":
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=BlogModelForm()
    return render(request,'form_create.html',{'form':form})

def detail(request,blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog_detail':blog_detail})