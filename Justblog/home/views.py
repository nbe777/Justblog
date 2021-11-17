from django.shortcuts import render,redirect
from .models import BlogModel,CommentModel
from .forms import BlogForm,CommentForm
from accounts.models import UserProfile
from django.shortcuts import get_object_or_404

def home(request):
    obj = BlogModel.objects.all()
    context = {'blogs':obj}
    return render(request,'Justblog.html',context)

def blogdetails(request,pk):
    id=pk
    obj = BlogModel.objects.get(id=id)
    com = CommentModel.objects.filter(blog = obj)
    user= request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            blogcomment=CommentModel.objects.create(comment=form.cleaned_data['comment'],rating=form.cleaned_data['rating'],name=user.username,blog=obj)
            blogcomment.save()
            profile = UserProfile.objects.get(user=obj.user)
            context = {'blog':obj,'comments':com, 'forms': CommentForm,'profile':profile}
            return render(request,'blogdetails.html',context)

    else:
        profile = UserProfile.objects.get(user=obj.user)
        context = {'blog':obj,'comments':com, 'forms': CommentForm,'profile':profile}
        return render(request,'blogdetails.html',context)



def addblog(request):
    if request.method == 'POST':
        user = request.user
        if user is None:
            return redirect('register')
        else:
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                subtitle = form.cleaned_data['subtitle']
                blog_content = form.cleaned_data['blog_content']
                image = form.cleaned_data['image']
                obj = BlogModel.objects.create(user=user,title=title,subtitle=subtitle,blog_content=blog_content,image=image)
                return redirect('/')

    else:
        context = {'form':BlogForm}
        return render(request,'addblog.html', context)

def seelistblog(request):
    blogobj = BlogModel.objects.filter(user=request.user)
    context = {'Bloglist':blogobj}
    return render(request,'seelistblog.html',context)

def update(request,pk):
    id=pk
    blogobj = BlogModel.objects.get(id=id)
    initial_dic = {'title':blogobj.title,'subtitle':blogobj.subtitle,'blog_content':blogobj.blog_content}
    forms = BlogForm(initial=initial_dic)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        user = request.user
        id=pk
        if form.is_valid():
            title = form.cleaned_data['title']
            subtitle = form.cleaned_data['subtitle']
            blog_content = form.cleaned_data['blog_content']
            image = form.cleaned_data['image']
            obj = get_object_or_404(BlogModel, id=id)
            obj.user = user
            obj.title = title
            obj.blog_content = blog_content
            obj.image = image
            obj.save()
            return redirect('/')
    else:
        context={'form':forms}
        return render(request,'updateform.html', context)


def delete(request,pk):
    id=pk
    blogobj = BlogModel.objects.get(id=id)
    blogobj.delete()
    return redirect('seelistblog')

def profile(request,pk=None):
    id=pk
    blog = BlogModel.objects.get(id=id)
    profile = UserProfile.objects.get(user=blog.user)
    context={'blog':blog, 'prof':profile}
    return render(request,'profile.html',context)

def myprofile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    context={'profile':profile}
    return render(request,'myprofile.html',context)
