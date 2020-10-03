from django.shortcuts import render
from app.models import Post

def home(request):
    context = Post.objects.all()
    return render(request,'home.html',{'data': context})