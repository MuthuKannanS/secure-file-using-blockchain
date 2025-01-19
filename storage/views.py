from django.shortcuts import render,redirect
from .models import data_uploader,data_receiver,files,request_files
from django.views import generic
from django.contrib import messages
import hashlib
from datetime import datetime
import random

from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'main.html')

def userlogin(request):
    return render(request,'index1.html')

def receiverlogin(request):
    return render(request,'index2.html')
    
def register1(request):
    return render(request,"register1.html")

def register2(request):
    return render(request,"register2.html")

def signup1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        m = data_uploader(username=username, password=password)
        m.save()
        return redirect(userlogin) 
    else:
        return redirect(register1)
        
def signup2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        mail = request.POST['mail']
        m = data_receiver(username=username, password=password, mail=mail)
        m.save()
        return redirect(receiverlogin) 
    else:
        return redirect(register2)        

def login1(request):
    username = request.POST['username']
    password = request.POST['password']
    if request.method == 'POST':
        try:
            r = data_uploader.objects.get(username=username)
            if r.username == username:
                if r.password == password:
                    id = r.id
                    m = files.objects.all()
                    try:
                        h = request_files.objects.filter(uploader_name=username)
                        context = {'id':id,'username':username,'m':m,'h':h}
                        return render(request,'main1.html',context) 
                    except request_files.DoesNotExist:
                        context = {'id':id,'username':username,'m':m}
                        return render(request,'main1.html',context)    
                else:
                    return render(request,'index1.html')           
            else:
                return render(request,'index1.html')  
        except data_uploader.DoesNotExist:
            return render (request, 'index1.html')  
    else:
        return render(request,'index1.html') 

def login2(request):
    username = request.POST['username']
    password = request.POST['password']
    if request.method == 'POST':
        try:
            r = data_receiver.objects.get(username=username)
            if r.username == username:
                if r.password == password:
                    id = r.id
                    m = files.objects.all()
                    try:
                        h = request_files.objects.filter(receiver_name=username)
                        context = {'id':id,'username':username,'m':m,'h':h}
                        return render(request,'main2.html',context) 
                    except request_files.DoesNotExist:
                        context = {'id':id,'username':username,'m':m}
                        return render(request,'main2.html',context)      
                else:
                    return render(request,'index2.html')           
            else:
                return render(request,'index2.html')  
        except data_receiver.DoesNotExist:
            return render (request, 'index2.html')  
    else:
        return render(request,'inedx2.html') 
        
def back(request,id):
    r = data_receiver.objects.get(id=id)
    username = r.username
    m = files.objects.all()
    h = request_files.objects.filter(receiver_name=username)
    context = {'id':id,'username':username,'m':m,'h':h}
    return render(request,'main2.html',context)
        
def logout(request):
    return redirect(index)

def main(request):
    return render(request,"main.html")

def upload(request,id):
    if request.method == 'POST':
        m = data_uploader.objects.get(id=id)
        username = m.username
        filename = request.POST['filename']
        file_field = request.FILES['file']
        print(file_field)
        path = r'media/' +str(file_field)
        BLOCK_SIZE = 65536
        file_hash = hashlib.sha256()
        with open(path, 'rb') as f:
            fb = f.read(BLOCK_SIZE)
            while len(fb)>0:
                file_hash.update(fb)
                fb = f.read(BLOCK_SIZE)
        hash_value = file_hash.hexdigest()
        date_time = datetime.now()
        n = random.randint(1,1000000)
        instance = files(username=username, key=n,filename=filename, file=file_field, hash_value=hash_value, date_time=date_time)
        instance.save()
        m = files.objects.all()
        h = request_files.objects.filter(uploader_name=username)
        context = {'id':id,'username':username,'m':m,'h':h}
        messages.success(request, 'Files Submitted successfully!')
        return render(request,'main1.html',context)
    else:
        messages.error(request, 'Files was not Submitted successfully!')
        return render(request,"main.html")
        
def request(request,id1,id):
    u = data_receiver.objects.get(id=id)
    username = u.username
    print(username)
    f = files.objects.get(filename=id1)
    filename = id1
    username1 = f.username
    m = request_files(uploader_name=username1 ,filename=filename, receiver_name=username )
    m.save()
    m = files.objects.all()
    h = request_files.objects.filter(receiver_name=username)
    context = {'id':id,'username':username,'m':m,'h':h}
    messages.success(request, 'Send request to Data uploader')
    return render(request,'main2.html',context)
def send_email(request,name,id):
    l = request_files.objects.get(filename=name)
    filename = l.filename
    receiver_name = l.receiver_name
    q = data_receiver.objects.get(username=receiver_name)
    email = q.mail
    k = data_uploader.objects.get(id=id)
    username = k.username
    m = files.objects.all()
    h = request_files.objects.filter(receiver_name=username)
    context = {'id':id,'username':username,'m':m,'h':h}
    r = files.objects.get(filename=name)
    key = r.key
    subject = ("File name & Your requset file Key ")
    message = filename + key
    send_mail(
        subject,
        message,
        'nsnagaraj10062002@gmail.com',
        [email],
        fail_silently=False,
    )
    messages.success(request, 'Send key to Data receiver Mail')
    return render(request,'main1.html',context)
    
def download(request,id1):
    id = id1
    if request.method == 'POST':
        filename = request.POST['filename']
        key = request.POST['key']
        try:
            u = files.objects.get(filename=filename)
            if u.key == key:
                file = u.file
                context = {'id':id,'filename':filename,'key':key,'file':file}
                return render(request,'download.html',context) 
            else:
                return redirect(index)
        except files.DoesNotExist:   
            return redirect(index)
    else:
        return redirect(index)
        
  
