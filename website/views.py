from django.shortcuts import render
from .models import Post, Created, Contact

def hello_blog(request):
    data = {}
    data['posts'] = Post.objects.filter(deleted=True)
    data['create'] = Created.objects.filter(id=1)
    return render(request, 'index.html', data)

def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_details.html', {'post': post})

def save_form(request):
    req = request.POST
    Contact.objects.create(name=req['name'], email=req['email'], message=req['message'])
    return render(request, 'contact_sucess.html', {'req': req['name']})
