from django.shortcuts import render, redirect
from App.models import Posts, Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')

def addpost(request):
    return render(request,'addpost.html')

def posts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        content = request.POST.get('content')
        post = Posts(name=name, title=title, slug=slug, content=content)
        post.save()

    posts = Posts.objects.filter().all()

    blogdict = {
        "posts": posts
    }
    return render(request, 'posts.html', blogdict)

def blog(request, slug):            
    blogposts = Posts.objects.filter(slug=slug).all()
    all_dict = {"blogposts": blogposts}
    return render(request, 'blogpost.html', all_dict)

def delete(request, slug):
    delete = Posts.objects.filter(slug=slug).delete()
    return  redirect("/posts/")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name,email=email,phone=phone,message=message)
        contact.save()

        messages.success(request,"Your message has been sent")
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')