from django.shortcuts import render,redirect
from .models import BlogModel,CommentModel
from .forms import BlogForm,CommentForm

# Create your views here.
def home(request):
    blogs = BlogModel.objects.all()
    if request.method == "POST":
        data = BlogForm(request.POST)
        if data.is_valid():
            data.save()
            fm = BlogForm()
            msg = "Blog Created"
            context = {
                "fm":fm,
                "msg":msg,
                "blogs":blogs
            }
            return render(request,'home.html',context)
        else:
            msg = data
            return render(request,'home.html',{"msg":msg,"blogs":blogs})
    else:
        fm = BlogForm()
        return render(request,'home.html',{"fm":fm,"blogs":blogs})
    
def blog(request,id):
    blog = BlogModel.objects.get(id=id)
    comments = CommentModel.objects.filter(post=blog)
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid():
            new_comment = comment.save(commit=False)
            new_comment.post = blog
            new_comment.save()
            return redirect("blog",id=blog.id)
        else:
            msg = comment
            return render(request,'blog.html',{"blog":blog,"msg":msg})
    else:
        comment = CommentForm
        return render(request,'blog.html',{"blog":blog,"comment":comment,"comments":comments})