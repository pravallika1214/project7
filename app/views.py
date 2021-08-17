from django.shortcuts import render

# Create your views here.
def hai(request):
    return render(request,'app.html',context={'name':'valli','age':20})

def hello(request):
    return render(request,'app.html',context={'name':'naveen','age':20})