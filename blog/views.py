from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogForm
# Create your views here.

#CRUD 중 Read기능
def home(request):
    # blogs = Blog.objects.all() --> 모든 Blog객체를 가져온다.

#filter기능 사용하기 위해서 만듬
    blogs = Blog.objects.order_by('-pub_date') # Blog객체를 최신 순으로 가져온다.
    search = request.GET.get('search')
    if search == 'true':
        author = request.GET.get('writer')
        blogs = Blog.objects.filter(writer=author).order_by('-pub_date') 
         #filter는 writer가 author인 것만 가져오는 것이고, filter 대신 exclude를 사용하면 writer가 author인 것만 제외하고 가져올 것이다.
#filter기능 사용하기 위해서 만듬

    paginator = Paginator(blogs, 3) #import받은 Paginator를 이용해서 객체를 3개씩 나눈다.
    page = request.GET.get('page') #여러 페이지중 몇번째 페이지를 받을 것인지 받는다.
    blogs = paginator.get_page(page) #여러 페이지중 요청받은 페이지를 받는다.
    return render(request, 'home.html', {'blogs':blogs}) # 해당 페이지를 넘겨준다.

#CRUD 중 Read기능
def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request,'detail.html',{'blog':blog})

#CRUD 중 Create기능
def new(request):
    form = BlogForm() #django에서 제공하는 forms 활용
    return render(request, 'new.html', {'form':form}) #form을 넘겨줌
    
#CRUD 중 Create기능
def create(request):
    form = BlogForm(request.POST, request.FILES)# django에서 제공하는 forms 활용
    if form.is_valid():
        new_blog = form.save(commit = False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)
    return redirect('home')

    # new_blog = Blog()
    # new_blog.title = request.POST['title']
    # new_blog.writer = request.POST['writer']
    # new_blog.body = request.POST['body']
    # new_blog.image = request.FILES['image']
    # new_blog.pub_date = timezone.now()
    # new_blog.save()
    # return redirect('detail',new_blog.id)


def edit(request, id):
    edit_blog = Blog.objects.get(id = id)
    return render(request, 'edit.html',{'blog':edit_blog})

def update(request, id):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        update_blog = form.save(commit = False)
        update_blog.pub_date = timezone.now()
        update_blog.save()
        return redirect('detail', update_blog.id)
    return redirect('home')

    # update_blog = Blog.objects.get(id = id)
    # update_blog = Blog()
    # update_blog.title = request.POST['title']
    # update_blog.writer = request.POST['writer']
    # update_blog.body = request.POST['body']
    # update_blog.image = request.FILES['image']
    # update_blog.pub_date = timezone.now()
    # update_blog.save()
    # return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('home')