from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import *
from myapp.forms import *
# Create your views here.
def create_topic(request):
    if request.method=="POST":
        topic=request.POST.get("topic")
        t=Topic.objects.get_or_create(topic_name=topic)
        if t[1]==True:
            t[0].save()
            return HttpResponse("<h2>Topic Added Successfully</h2>")
        else:
            return HttpResponse("<h2>Topic Is Already Exist In Table</h2>")
    return render(request,"create_topic.html")

def create_webpage(request):
    if request.method=="POST":
        topic=request.POST.get('topic')
        name=request.POST.get('name')
        url=request.POST.get("url")
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        w=Webpage.objects.get_or_create(topic=t,name=name,url=url)[0]
        w.save()
        return HttpResponse("<h2>Webpage Added Successfully</h2>")
    topics=Topic.objects.all()
    return render(request,"create_webpage.html",context={'topics':topics})
def display_topics(request):
    topics=Topic.objects.all()
    return render(request,"display_topic.html",context={'topics':topics})
def display_webpages(request):
    webpages=Webpage.objects.all()
    return render(request,"display_webpage.html",context={'webpages':webpages})
def display_topic(request,id):
    topics=Topic.objects.filter(id=id)
    return render(request,"display_topic.html",context={'topics':topics})
def display_webpage(request,wid):
    webpages=Webpage.objects.filter(id=wid)
    return render(request,"display_webpage.html",context={'webpages':webpages})
def create_access(request):
    if request.method=="POST":
        webpage=request.POST.get("webpage")
        datetime=request.POST.get("datetime")
        w=Webpage.objects.get_or_create(name=webpage)[0]
        d=AccessDetails.objects.get_or_create(webpage=w,datetime=datetime)[0]
        d.save()
        return HttpResponse("<h1>DateTime Added Successfully</h1>")
    webpages=Webpage.objects.all()
    return render(request,"create_access.html",context={'webpages':webpages})
def display_access1(request):
    accessdetails=AccessDetails.objects.all()
    return render(request,"display_access.html",context={'accessdetails':accessdetails})
def display_access(request,aid):
    accessdetails=AccessDetails.objects.filter(id=aid)
    return render(request,"display_access.html",context={'accessdetails':accessdetails})
def search(request):
    if request.GET.get('search'):
        id=request.GET['search']
        return redirect('display_webpage',webid=id)
    return render(request,'search.html')
    
def update_topic(request,id):
    if request.method=="POST":
        new_tname=request.POST.get("topic_name")
        t=Topic.objects.filter(id=id).update(topic_name=new_tname)
    t=Topic.objects.get(id=id)
    return render(request,"update_topic.html",{"topic":t})

def update_webpage(request,id):
    if request.method=="POST":
        topic=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        t=Topic.objects.get(topic_name=topic)
        w=Webpage.objects.filter(id=id).update(topic=t,name=name,url=url)
    t=Topic.objects.all()
    webpage=Webpage.objects.get(id=id)
    return render(request,"update_webpage.html",{"topics":t,'webpage':webpage})
def delete_topic(request,id):
    t=Topic.objects.filter(id=id)
    if t:
        t.delete()
        return HttpResponse("<h1>deletion is successful </h1>")
    return HttpResponse("<h1>Record not found </h1>")
def delete_webpage(request,wid):
    w=Webpage.objects.filter(id=wid)
    if w:
        w.delete()
        return HttpResponse("<h1>deletion is successful </h1>")
    return HttpResponse("<h1>Record not found </h1>")
def disp_img(request,pid):
    profile=ProfilePic.objects.get(id=pid)
    return render(request,"display_image.html",{'profile':profile})
def topic_modelform(request):
    if request.method=="POST":
        form=TopicForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'modelform.html',{'form':form})
    form=TopicForm()
    return render(request,'modelform.html',{'form':form})
def webform(request):
    if request.method=="POST":
        form=WebpageForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'modelform.html',{'form':form})
    form=WebpageForm()
    return render(request,'modelform.html',{'form':form})
def create_user(request):
    if request.method=="POST":
        user=UserModelForm(request.POST)
        if user.is_valid():
            password=user.cleaned_data['password']
            user=user.save(commit=False)
            user.set_password(password)
            user.save()
    form=UserModelForm()
    return render (request,"modelform.html",{'form':form})