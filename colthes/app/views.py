from django.shortcuts import render,redirect,get_object_or_404
from .models import clothes,Profile,CustomerReview,Message
from .models import order
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def about(request):
    return render(request,'about.html',)
def serv(request):
    return render(request,'serv.html',)
def contact(request):
    error=''
    if request.method=='POST':
        a=request.POST
        name=a.get('name')
        email=a.get('email')
        subject=a.get('subject')
        message=a.get('message')
        if not name:
            error='please enter your name'
        elif not email:
            error='please enter your email'
        elif not subject:
            error='enter your subject'
        elif not message:
            error='enter your message'
        else:
            error='successfully'
        data=Message(
            name=name,
            subject=subject,
            email=email,
            message=message
        )
        data.save()
    return render(request,'cantact.html',{'i':error})
def home(request):
    data=clothes.objects.all()[:15]
    data1=clothes.objects.all()[15:30]
    data3=clothes.objects.all()
    if request.method=="GET":
        search=request.GET.get('search')
        if search:
            data3=clothes.objects.filter(cloth_name__icontains=search)
            return render(request,'home.html',{'search':data3})
            # return redirect('home')
    return render(request,'home.html',{'i':data,'a':data1})
 


def sign_up(request):
    a=''
    if request.method=='POST':
        a=request.POST
        name=a.get('name')
        email=a.get('email')
        pass1=a.get('pass1')
        pass2=a.get('pass2')
        role=a.get('opt')
        if pass1!=pass2:
            a='password does not match'
        elif not name:
            a='please enter your name'
        elif not pass1:
            a='please enter your name'
        else:
            user=User.objects.create_user(name,email,pass1)
            user.save()
            user.profile.role = role
            user.profile.save()
            return redirect('login')

    return render(request,'signup.html',{'error':a})

def login_e(request):
    error=''
    if request.method=='POST':
        name=request.POST.get('name')
        pass1=request.POST.get('pass')
        user=authenticate(username=name,password=pass1)
        if user is not None:
            login(request,user)
            if user.profile.role == 'seller':
                return redirect('user1')#, id=user.id)
            else:
                return redirect('home')
        if user is None:
            error='user not found'
        else:
            if user.username!=name and user.password!=pass1:
                error='your name and password soes not match '  
            # return redirect('user1',id=user.id)
    return render(request,'login.html',{'error':error})

def user_data(request):
    error=''
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    user=get_object_or_404(User, username=request.user.username)
    

    if request.method=='POST':
        a=request.POST
        
        image=request.FILES.get('image')
        cloth_name=a.get('cloth_name')
        fashion_name=a.get('fashion_name')
        price=a.get('price')
        if not image:
            error='please enter your product image'
        elif not cloth_name:
            error='please enter product name'
        elif not fashion_name:
            error='please enter fashion name'
        elif not price:
            error='please enter your product price'
        else:

            data11=clothes(
            user=user,
            image=image,
            cloth_name=cloth_name,
            fashion_name=fashion_name,
            price=price
            )
            data11.save()
            return redirect('user1') #id=user.id)
    data=clothes.objects.filter(user=user)
    # cloth = clothes.objects.get(id=id)
    orders=order.objects.filter(relation__in=data)
    return render(request,'user.html',{"i":data,'error':error,'order':orders})



#cart page summerization

def cart1(request,id):
    data=get_object_or_404(clothes,id=id)
    
    error=''
    if request.method=='POST':
        a=request.POST
        form=a.get('form_type')
        if form =='order':
           quantity=a.get('qty')
           cloth_name=a.get('cloth_name')
           size=a.get('size')
           email=a.get('email')
           phone=a.get('phone')
           address=a.get('address')
           color=a.get('color')

           if cloth_name.strip().lower() != data.cloth_name.strip().lower():
               error='please correct cloth name'
           elif not quantity:
               error='please enter quantity'
           elif not cloth_name:
               error='please enter a cloth name'
           elif not email:
               error='please enter email'
           elif not phone:
               error='please enter phone number'
           elif not address:
               error='please enter your address'

           else:
        #    if not error:
               order_data=order(
            # id=id,
            relation=data,
            quantity=quantity,
            cloth_name=cloth_name,
            size=size,
            email=email,
            phone=phone,
            address=address,
               )
               order_data.save()
               return redirect('cart_page',id=id)
        
    if request.method=='POST':
        a=request.POST
        form=a.get('form_type')
        if form == 'review':
           info=a.get('info')
           data1=CustomerReview(
            khan=data,
    
            info=info,
            user=request.user

            )
           data1.save()
           return redirect('cart_page', id=id)
    reviews = CustomerReview.objects.filter(khan=data)
    

    return render(request,'cart_page.html',{'i':data , 'error':error,'reviews':reviews,})






