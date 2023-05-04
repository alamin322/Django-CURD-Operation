from django.shortcuts import render, HttpResponseRedirect
from .models import UserInfo
# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        # print(name, email, phone)
        user_info = UserInfo(name=name, email=email, phone=phone)
        user_info.save()
        
    information = UserInfo.objects.all().order_by('id')
        
    # print(information)
    
    context = {'information': information}
    
    return render(request, 'app1/index.html', context=context)

def delete_info(request, id):
    if request.method == "POST":
        user_info = UserInfo.objects.get(pk=id)
        user_info.delete()
    
    return HttpResponseRedirect('/')

def update_info(request, id):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        # print(name, email, phone)
        
        
        
        user_info = UserInfo.objects.get(pk=id)
        user_info.name = name
        user_info.email = email
        user_info.phone = phone
        
        user_info.save()
        
        return HttpResponseRedirect('/')
    
    return render(request, 'app1/update_info.html')