from threading import local
from django.shortcuts import render
from .models import student,score

# Create your views here.
def listscore(request):
    try:
        students = score.objects.all()
    except:
        errormessage = '錯誤'
    return render(request,'listscore.html',locals())

def listone(request,sname):
    unit = student.objects.get(name=sname)
    return render(request,'listone.html',locals())

def listall(request):
    try:
        students = student.objects.all()
    except:
        errormessage = '錯誤'
    return render(request,'listall.html',locals())


def insert(request):
    if request.method =='POST':
        name = request.POST['name']
        sex = request.POST['sex']
        birth = request.POST['birth']
        email = request.POST['email']
        phone = request.POST['phone']
        chinese = request.POST['chinese']
        math = request.POST['math']
        english = request.POST['english']
        nature = request.POST['nature']

        unit = student.objects.create(name=name,sex=sex,birth=birth,email=email,phone=phone)
        unit.save()
        sunit = score.objects.create(sname=name,chinese=chinese,math=math,english=english,nature=nature)
        sunit.save()

        return render(request,"insert.html",locals())
    else:
        return render(request,'insert.html',locals())

def index(request):
    return render(request,'index.html',locals())

def modify(request,sname):
    unit = student.objects.get(name=sname)
    if request.method == 'POST':
        unit.name = request.POST['sname']
        unit.sex = request.POST['ssex']
        birthday = request.POST['sbirth']
        birth = ((birthday.replace('年','-')).replace('月','-')).replace('日','')
        unit.birth = birth
        unit.email = request.POST['semail']
        unit.phone = request.POST['sphone']
        unit.save()
        students = student.objects.all()
        return render(request,'listall.html',locals())
    else:
        name = unit.name
        sex = unit.sex
        birth = unit.birth
        email = unit.email
        phone = unit.phone
        return render(request,'modify.html',locals())

def modifyscore(request,sname):
    unit = score.objects.get(sname=sname)
    if request.method == 'POST':
        unit.chinese = request.POST['chinese']
        unit.math = request.POST['math']
        unit.english = request.POST['english']
        unit.nature = request.POST['nature']
        unit.save()
        students = score.objects.all()
        return render(request,'listscore.html',locals())
    else:
        chinese = unit.chinese
        math = unit.math
        english = unit.english
        nature = unit.nature
        return render(request,'modifyscore.html',locals())

def delete(request,sname):
    unit = student.objects.get(name=sname)
    unit.delete()

    sunit = score.objects.get(sname=sname)
    sunit.delete()
    students = student.objects.all()
    return render(request,'listall.html',locals())