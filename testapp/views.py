
# from DjangoLogin.testapp import forms
from queue import Empty
from django.shortcuts import redirect, render
# from DjangoLogin.testapp import models
from testapp.forms import RegistrationUser,ans_form
from  django.contrib.auth.decorators import login_required
from testapp.models import Q,Java
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

@login_required

def python_view(request):     
    list=Q.objects.all()
    # form=ans_form()
    if request.method =="POST":
        print(list)
        count=0
        d1={}

        for q in list:
            print(d1[q])
            try:
            # request.session[str(q.id)]=request.POST["que"+str(q.id)]
                d1[q.id]=request.POST['question_'+str(q.id)]
            except Exception :
                print("Someting went wrong")



        for q in list:
            print("User Entered ans: ",request.session[str(q.id)])
        
        for q in list:
            que=Q.objects.get(pk=q)
            correct_ans=que.correctop
            print("Correct ans is:",correct_ans)
            # if request.session[str(q.id)]==correct_ans:
            #     count=count+1
            if d1[q] == correct_ans:
                count=count+1
                return render(request,'testapp/result.html',{'marks':count})
        print("Count: ",count)
    


    # paginator=Paginator(list,1)
    # page_num=request.GET.get('page')
    # page=paginator.get_page(page_num)

    # try:
    #     list=paginator.page(page_num)
    # except PageNotAnInteger:
    #     list=paginator.page(1)
    # except EmptyPage:
    #     list=paginator.page(paginator.num_pages)
    context={"list":list}
    return render(request,'testapp/python.html',context)
    # return render (request,"testapp/java.html",{"form":form})

# def demo(request):
#     form=ans_form()
#     if request.method=='POST':
#         form=ans_form(request.POST)
#         if form.is_valid():
#             Qta1=request.POST['Qta1']
#             op1=request.POST['op1']
#             print("yes working")
#             request.session[Qta1]=op1

    #         # form=request.POST.get('form',False)
    #         # # cr=request.GET['correctop']
    #         # request.session['form']=form
    # return render(request,'testapp/register.html',{"form":form})

# def demo_show(request):
#     return render(request,"testapp/demoresult.html")
@login_required

def java_view(request):
    list=Java.objects.all()
    # form=ans_form()
    if request.method =="POST":
        print(list)
        count=0
        d1={}

        for q in list:
            print(d1[q])
            try:
            # request.session[str(q.id)]=request.POST["que"+str(q.id)]
                d1[q.id]=request.POST['question_'+str(q.id)]
            except Exception :
                print("Someting went wrong")

        for q in list:
            print("User Entered ans: ",request.session[str(q.id)])
        
        for q in list:
            que=Java.objects.get(pk=q)
            correct_ans=que.correctop
            print("Correct ans is:",correct_ans)
            # if request.session[str(q.id)]==correct_ans:
            #     count=count+1
            if d1[q] == correct_ans:
                count=count+1
                return render(request,'testapp/result.html',{'marks':count})
        print("Count: ",count)
    
    context={"list":list}
    return render(request,'testapp/java.html',context)

def logout_view(request):
    return render(request,'testapp/logout.html')

def registration_view(request):
    forms=RegistrationUser()
    if request.method == 'POST':
        forms=RegistrationUser(request.POST)
        if forms.is_valid():
            user=forms.save();
            user.set_password(user.password)
            user.save()
            return redirect('/')
    return render(request,'testapp/register.html',{'forms':forms})
