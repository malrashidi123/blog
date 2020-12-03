from django.shortcuts import render, HttpResponse,  redirect
from .models import *
from .forms import *
# Create your views here.
def post_list(request):
	post = Post.objects.all()

	return render(request, 'post_list.html', {'posts': post})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_new(request):
    print(request)
    if request.method == "POST":
        print('pass.method')
        form = PostForm(request.POST)
        if form.is_valid():
            print(form)
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})
    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})