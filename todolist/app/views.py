from django.shortcuts import render,redirect
from .models import List,List1

# Create your views here.
def parrot(request):
    if request.method == "POST":
        task = request.POST.get("task")
        desc = request.POST.get("desc") 
        List.objects.create(taskname = task,taskdesc = desc)
        return redirect('task')
    return render(request,'list.html')


def list(request):
    d1 = List.objects.all()
    context= {
        'data':d1
    }
    return render(request,'desc.html',context)

def task(request,pk):
    b = List.objects.get(id=pk)
    if request.method == "POST": 
        c = b.taskname
        d = b.taskdesc
        print(b)
        List1.objects.create(taskname = c , taskdesc = d)
        b.delete()
        return redirect('program')
    context = {
        'data':b
    }
    return render(request,'details.html',context)   

def display(request,pk):
    a = List.objects.get(id=pk)
    if request.method == "POST":
        task = request.POST.get("taskname")
        desc = request.POST.get("taskdesc")  
        a.taskname = task
        a.taskdesc = desc
        print(a.taskname,a.taskdesc)
        a.save()
        return redirect('task')
    context = {
        'data' : a
    }
    return render(request,'edit.html',context)

def oops(request):
    a1 = List1.objects.all()
    context = {
        'data':a1
    }
    return render(request,'history.html',context)