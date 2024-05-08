from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

from .form import CommentForm
from .models import Author, About, Post, Comment, SocialMedia

# Create your views here.


def home_page(request):
    author = Author.objects.all().order_by('id')[:1]
    posts = Post.objects.all().order_by('-id')[:3]
    socials = SocialMedia.objects.all()
    context = {'authors': author, 'posts': posts, 'socials': socials}
    return render(request, 'index.html', context)


def blog_page(request):
    posts = Post.objects.all().order_by('-id')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts}
    return render(request, 'blog.html', context)


def blog_detail_page(request, pk):
    form = CommentForm()
    post = get_object_or_404(Post, pk=pk)
    tags = post.tags.all()
    tag = request.GET.get('tags')
    comments = Comment.objects.filter(post__id=pk).order_by('-id')
    if tag:
        post = post.tags.filter(tags__name=tags)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            print(comment.email)
            comment.post = post
            comment.save()
            return redirect(f"/detail/{post.id}/")
    else:
        form = CommentForm()
    context = {'post': post,
               'form': form,
               'comments': comments,
               'tags': tags,
               'tag': tag}
    return render(request, 'blog-single.html', context)


def about_page(request):
    author = Author.objects.all().order_by('id')[:1]
    abouts = About.objects.all().order_by('id').all()
    socials = SocialMedia.objects.all()
    context = {'author': author, 'abouts': abouts, 'socials': socials}
    return render(request, 'about.html', context)

