from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Blogs
from django.http import HttpResponse, HttpResponseRedirect
# from datetime import date
import datetime
from .forms import add_blog


def blog(request,):
    blogs = Blogs.objects.all().order_by('-id')
    params = {'blogs': blogs}
    return render(request, "blog/index.html", params)

def blogpost(request,id):
    blog = Blogs.objects.get(id=id)
    blogger = blog.blogger
    params = {'blog': blog, 'blogger': blogger}
    return render(request, "blog/post.html", params)

# ---------------------------------------------------------------------
# vendor related functions
# ---------------------------------------------------------------------

@login_required(login_url="../login")
def addblog(request):
    if request.user.is_Blogger:
        if request.method == 'POST':
            form = add_blog(request.POST, request.FILES)
            if form.is_valid():
                content = form.cleaned_data['content']
                image = form.cleaned_data['image']
                title = form.cleaned_data['title']
                blogger = getblogger(request.user.email)
                # pub_date = date.today()
                pub_date = datetime.datetime.now()
                cont = Blogs.objects.create(image=image, content=content, blogger=blogger, title=title, pub_date=pub_date)
                cont.save()
                msg="Blog Successfully Posted"
                return render(request, 'blog/addblog.html', {'form': form,"msg":msg})
        else:
            form = add_blog()
            msg=""
            return render(request, 'blog/addblog.html', {'form': form, "msg": msg})
    else:
        return render(request, "shop/unauthorized.html")



