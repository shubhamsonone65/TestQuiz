from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import Question,student,Quiz
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import date,time
import json
from datetime import datetime

# Create your views here.

timerecord=[]
timerecord2=[]

def home(request):
    timerecord2.clear()
    timerecord.clear()
    categories={}
    allobjects=Question.objects.all()
    for objects in allobjects:
        categories[objects.category]=objects.category
    ids.clear()
    return render(request,'quizhome.html',{'categories':categories})

ids=[]

def quizpage(request,category,num):
    if request.user.is_authenticated:
        if num==1 or num==len(ids)+1:
            if num==1:
                timenow=datetime.now()
                timerecord.append(timenow)
                ids.clear()
            if category=='all':
                quizQuestions=list(Question.objects.all().exclude(id__in=ids))
            else:
                quizQuestions=list(Question.objects.filter(category=category).exclude(id__in=ids))
            x=(random.randint(1,len(quizQuestions)))
            que=(quizQuestions[x-1])
            ids.append(quizQuestions[x-1].id)
            answers=[]
            currect=Question.objects.get(id=quizQuestions[x-1].id).Correctop
            answers.append(currect)
            answers.append(Question.objects.get(id=quizQuestions[x-1].id).wrongop1)
            answers.append(Question.objects.get(id=quizQuestions[x-1].id).wrongop2)
            answers.append(Question.objects.get(id=quizQuestions[x-1].id).wrongop3)
            random.shuffle(answers)
            if num==10:
                ids.clear()
                return render(request,'quizpage.html',{'num':99,'category':category,'que':que,'answers':answers})
            
            return render(request,'quizpage.html',{'num':num+1,'category':category,'que':que,'answers':answers})
        ids.clear()
        messages.error(request,'quiz has been ended, false navigation not allowed')
        return redirect('/')
    else:
        messages.error(request,'You need to login before starting quiz...')
        return redirect('/')

    
def check(request,queid):
    que=Question.objects.get(id=queid)
    if request.is_ajax():
        data=request.POST
        if que.Correctop==data['answer']:
            return JsonResponse({'msg':'right','ans':data['answer']})
        else:
            return JsonResponse({'msg':'wrong','ans':data['answer']})

    else:
        return render(request,'error.html')

# @login_required('/')
def result(request):
    if request.is_ajax():
        data=request.POST
        data=dict(data)
        score=int(data['score'][0])
        del data['score']
        timenow=datetime.now()
        timerecord2.append(timenow)
        studentacc=student.objects.get(email=request.user.email)
        newQuiz=Quiz.objects.create(student=studentacc,record=data,score=score)
        return JsonResponse({'msg':'success'})
    try:
        timeelapsed=(timerecord2[0]-timerecord[0])
        print(timeelapsed)
        quizresult=Quiz.objects.last()
        return render(request,'result.html',{'quizresult':quizresult,'timeelapsed':timeelapsed})
    except:
        return render(request,'error.html')

def quizhistory(request):
    studentacc=student.objects.get(email=request.user.email)
    quizrecord=Quiz.objects.filter(student=studentacc)
    return render(request,'quizhistory.html',{'quizrecord':quizrecord})

def userlogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            nameuser=User.objects.get(email=email.lower()).username
            user=authenticate(request,username=nameuser,password=password)
        except Exception as e:
            user=None
        if user is not None:
            login(request,user)
            messages.success(request,'Logged in successfully...')
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials...')
            return redirect('/')
    else:
        return render(request,'error.html')

def userlogout(request):
    logout(request)
    messages.success(request,'Logged out successfully...')
    return redirect('/')

def signup(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        mail=request.POST.get('mail')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        acc=None
        try:
            acc=student.objects.get(email=mail)
        except Exception as e:
            print(e)
        if acc!=None:
            messages.error(request,'account with this email already exists...')
        elif(pass1==pass2):
            name=fname+'_'+lname
            myuser = User.objects.create_user(name,mail,pass1)
            myuser.first_name= fname
            myuser.last_name= lname
            myuser.save()
            studentdata=student(studentacc=myuser,email=mail)
            studentdata.save()
            login(request,myuser)
            messages.success(request, 'account is successfully created...')
    else:
        return render(request,'error.html')
    return redirect('/')
