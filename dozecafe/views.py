from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from .models import Order,Coffee, Contact, Blog

# Create your views here.
def index(request):
    list1= Coffee.objects.all().order_by("-id")[:4]
    list2= Coffee.objects.all().order_by("-id")[4:8]
    list3= Coffee.objects.all().order_by("-id")[8:12]
    blogs=Blog.objects.all().order_by('-id')[:2]
    return render(request,"index.html",{"list1":list1,'list2':list2,'list3':list3,"blogs":blogs})

def about(request):
    return render(request,"about.html",{})

def blog(request):
    blogs=Blog.objects.all()
    return render(request,"blog.html",{"blogs":blogs})

def coffee(request):
    coffees =Coffee.objects.all()
    return render(request,"coffees.html",{"coffees":coffees})

def contact(request):
    if request.method== "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        msg = request.POST.get('message')
        contact = Contact.objects.create(name=name,phone_no=phone_no,email=email,message=msg)
        contact.save()
        messages.info(request, "Thank You for Contacting Us, We'll get back to you shortly")
        return redirect("/")
    return render(request,"contact.html",{})

def order(request,id):
    if request.method=="POST":
        quantity=request.POST.get('quantity')
        address=request.POST.get('address')
        coffee=Coffee.objects.get(id=id)
        current_user = User.objects.get(id=request.user.id)
        order= Order.objects.create(customer_name=current_user,address=address,product=coffee,quantity=int(quantity))
        order.save()
        messages.info(request, "Order placed successfully!")
        return redirect('/')

    else:
        coffee=Coffee.objects.get(id=id)
        return render(request,"order.html",{"coffee":coffee})
    
def signup(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=email).exists():
                messages.info(request,"Username is Already Used!")
                return redirect('/signup')
            else:
                user = User.objects.create_user(username=email,password= password, email=email, first_name=name)
                user.save()
                messages.info(request,"Your have successfully created account, Login Now!")
                return redirect('/login')
        else:
            messages.info(request,"Password Not matching!")
            return redirect('/signup')
        
    return render(request,"signup.html",{})

def login(request):
    if request.method== "POST":
        username = request.POST['email']
        password = request.POST['password']
        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print(f"User {username} is loged in")
            messages.info(request,"You are successfully Loged In")
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials!")
            print("Invalid Login details")
            return redirect("/login")

    else:
        return render(request, "login.html",{})

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("/")