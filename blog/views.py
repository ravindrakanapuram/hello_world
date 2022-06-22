from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .models import Post , Category
from django.db.models import Count
def index(request):
    return render(request,'blog/post/index.html')

#post views

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 6) 
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    q = request.GET.get('q',None)
    items = ''
    if q is None or q is " ":
        posts = Post.objects.all()
    elif q is not None:
        posts = Post.objects.filter(body__contains=q)
        return render(request,'blog/post/list.html',{'page':page,'posts': posts})
    return render(request,'blog/post/list.html',{'page':page,'posts': posts})
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    
    return render(request,'blog/post/detail.html',{'post': post})
def category(request,id):
    category = Category.objects.get(id=id)
    context = {'category':category}
    return render(request,'blog/post/category.html', context)
def about(request):
    return render(request,'blog/post/about.html')
def sug_posts(request):
    post_list =  Post.objects.filter(publish__year=2022)[:5]
    return render(request,'blog/suggested.html',{'post_list':post_list})



  





