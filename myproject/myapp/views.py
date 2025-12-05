from django.shortcuts import render, redirect
from .models import Course, Times
from django.db.models import Q
from .form import Courseform

def read(request):
    x = Course.objects.all()
    if request.method == "POST":
        search = request.POST.get('search', '')
        x = Course.objects.filter(Q(name__icontains=search) | Q(tutor__icontains=search))
    return render(request, 'read.html', {"reads": x})

def create(request):
    times_list = Times.objects.all()  

    if request.method == "POST":
        cname = request.POST.get('name')
        ctutor = request.POST.get('tutor')
        ccredits = request.POST.get('credits')
        cstudents = request.POST.get('students')
        ctime_id = request.POST.get('times')  
        ctime = Times.objects.get(id=ctime_id) if ctime_id else None

        Course.objects.create(
            name=cname,
            tutor=ctutor,
            credits=ccredits,
            students=cstudents,
            times=ctime
        )

        return redirect('read')

    return render(request, 'create.html', {"times_list": times_list})

def update(request, id):
    x = Course.objects.get(id=id)
    times_list = Times.objects.all()  

    if request.method == "POST":
        cname = request.POST.get('name')
        ctutor = request.POST.get('tutor')
        ccredits = request.POST.get('credits')
        cstudents = request.POST.get('students')
        ctime_id = request.POST.get('times')
        ctime = Times.objects.get(id=ctime_id) if ctime_id else None

        x.name = cname
        x.tutor = ctutor
        x.credits = ccredits
        x.students = cstudents
        x.times = ctime
        x.save()

        return redirect('read')

    return render(request, 'update.html', {"updates": x, "times_list": times_list})

def delete(request, id):
    x = Course.objects.get(id=id)
    x.delete()
    return redirect('read')

def courseforms(request):
    if request.method == "POST":
        form1 = Courseform(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('read') 
    else:
        form1 = Courseform()  
        redirect('read')
    return render(request, 'form.html', {'formdata': form1})

# # BUILT IN USER FORM

# def builtinuser(request):
#     if request.method == "POST"