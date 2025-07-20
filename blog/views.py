from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import PostForm


def get_post_list(request):
    posts = Post.objects.all()

    return render(request, 'blog/post_list.html', context={'posts': posts})


def get_post_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)

    context = {'post': post}

    return render(request, 'blog/post_detail.html', context)


def create_post(request):
    if request.method == "GET":
        form = PostForm()

        return render(request, 'blog/post_add.html', context={"form": form})
    
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save()
            print(post)

            return redirect('post_detail', post_id=post.id)
        else:
            return render(request, 'blog/post_add.html', context={"form": form})


def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            updated_post = form.save()

            return redirect("post_detail", post_id=updated_post.id)
        else:
            return render(request, 'blog/post_update.html', context={"form": form})

    form = PostForm(instance=post)

    return render(request, 'blog/post_update.html', context={"form": form})
