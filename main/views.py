from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student, Teacher, Products_table

@login_required
def home(request):
    return render(request, "home.html")

@login_required
def about(request):
    return render(request, "about.html")

@login_required
def contact(request):
    return render(request, "contact.html")


def student_form(request):
    if request.method=="POST":
        student_name=request.POST.get("student_name")
        student_age=request.POST.get("student_age")
        student_city=request.POST.get("student_city")
        student_email=request.POST.get("student_email")
        student_phone=request.POST.get("student_phone")
        student_subject=request.POST.get("student_subject")
        student_grade=request.POST.get("student_grade")
        student_hobby=request.POST.get("student_hobby")
        student_address=request.POST.get("student_address")
        enrollment_year=request.POST.get("enrollment_year")
        # Here I will wite the student model object with the data 
        student= Student(
        student_name=student_name,
        student_age=student_age,
        student_city=student_city,
        student_email=student_email,
        student_phone=student_phone,
        student_subject=student_subject,
        student_grade=student_grade,
        student_hobby=student_hobby,
        student_address=student_address,
        enrollment_year=enrollment_year

    )
        student.save()

    return render (request, "student_form.html")

#retrieve student Data

def student_list(request):
    students=Student.objects.all()
    context= {"students":students}
    return render(request, "student_list.html", context)

def product_listing(request):
    products = Products_table.objects.all()
    context = {"all_products": products}
    return render(request, "product_list.html", context)


#User registration
def register(request):
    if request.method == "POST":
        username= request.POST ['username']
        password= request.POST ['password']
        first_name= request.POST ['f_name']
        last_name= request.POST ['l_name']
        
        
        User.objects.create_user(
         username=username,
         password=password,
         first_name=first_name,
         last_name=last_name
    )
    

    return render (request, "register.html")
# This is the codde for loging  and when not registered shows no register or something similar 
def u_login (request):
    if request.method=="POST":
        user_name= request.POST ['username']
        u_password= request.POST ['password']
    
        user = authenticate(
            request,
            username = user_name,
            password = u_password
    )
    
        if user is not None:
         login(request, user)
         return redirect('home_path')
        else: 
            return render(request, "login.html",{"message": "Incorrect login credencials, try again"})  
    
    return render (request, "login.html")

def u_logout(request):
     logout(request)
     return redirect('login')
        