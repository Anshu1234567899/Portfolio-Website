from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import registrationforms
from services.models import services
from portfolio.models import portfolio
from django.core.paginator import Paginator
from contactinfo.models import Contactinfo
from userregister.models import Userregister
from django.core.mail import send_mail,EmailMultiAlternatives
def home(request):
    portfolioData=portfolio.objects.all()
    servicesData=services.objects.all().order_by('id') 
    paginator=Paginator(servicesData,1)
    page_number=request.GET.get('page')
    service=paginator.get_page(page_number)
    totalpage= service.paginator.num_pages
    if request.method=="GET":
        st=request.GET.get('search')
        
        if st!=None:
            servicesData=services.objects.filter(services_title__icontains=st)

    # send_mail(
    #     'Testing Mail',
    #     'hello i am deepanshu',
    #     'infou06@gmail.com',
    #     ['aganivayu@gmail.com'],
    #     fail_silently= False,
    # )


    # for a in servicesData:
    #     print(a.services_icon)
    #     print(a.services_title)
    #     print(a.services_des)
    # print(services)  
    data={
        'servicesData':service,
        'portfolioData':portfolioData,
        'lastpage': totalpage,
        'totalpagelist':[n+1 for n in range(totalpage)]
    }
    return render(request,"index.html",data)

def portfoliodetails(request,slug):
    
    portfolio_details=portfolio.objects.get(portfolio_slug=slug)
    data={
        'portfoliodetails':portfolio_details

    }
    
    return render(request,'portfoliodetails.html',data) 
    
def about(request):
    return render(request,"aboutus.html") 
def skill(request): 
    return render(request,"skill.html")
def project(request):
    return render(request,"project.html")
def contact(request):
    return render(request,"contact.html")
def saveinfo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        info=Contactinfo(name=name,email=email,message=message)
        info.save()

        subject = f"New message from {name}"
        from_email = 'infou06@gmail.com'  # your verified Gmail
        to_email = ['aganivayu@gmail.com']  # your admin email
        body = f"""
        <h3>New Contact Form Submission</h3>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Message:</strong><br>{message}</p>
        """

        msg = EmailMultiAlternatives(subject, body, from_email, to_email)
        msg.content_subtype = 'html'
        msg.extra_headers = {'Reply-To': email}  # ✅ So admin can reply directly to user
        msg.send()

        

    n=("Thank you for reaching out! Your message has been received successfully.Our team will get back to you as soon as possible. We appreciate your time!")
    return render(request,"contact.html",{'n':n})
    
def registration(request):
    
    try:
        if request.method=="POST":
            fullname=request.POST.get('fullname')
            email=request.POST.get('email')
            password=request.POST.get('password')
            gender=request.POST.get('gender')
            user=Userregister(fullname=fullname,email=email,password=password,gender=gender)
            user.save()
            return HttpResponseRedirect('/login/')
    except Exception as e:
        print("Error during registration:", e)
    return render(request,"registration.html",) 
def login(request):
    
    fn = registrationforms()
    data = {'form': fn}

    if request.method == "POST":
        fullname = request.POST.get('fullname')
        password = request.POST.get('password')

        try:
            user = Userregister.objects.get(fullname=fullname)

            if user.password == password:
                request.session['user_name'] = user.fullname
                return redirect('/')
            else:
                return render(request, 'login.html', {'form': fn, 'error': 'Invalid password'})

        except Userregister.DoesNotExist:
            return render(request, 'login.html', {'form': fn, 'error': 'User not found'})

    return render(request, 'login.html', data)
def detail(request):
    return HttpResponse(request)
def calculator(request):
    c=''
    try:
        if request.method=='POST':
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            operation=request.POST.get('operation')
            if operation=='add':
                c=n1+n2
            elif operation=='subtract':
                c=n1-n2
            elif operation=='multiply':
                c=n1*n2
            elif operation=='divide':
                c=n1/n2
            elif operation=='remainder':
                c=n1 % n2
    except:
       c=" Invalid operation...."
       print(c)    
    return render(request,'calculator.html',{'c':c})


def info(request):
    data={
        'name':'BharatBuilds',
        'title': 'Hey Fill this form and register yourself first.',
        'list': ('tech','ai','ml'),
        'numbers': (10,20,30,40,50),
        'user_details':(
             {'name' :'ansh','phone':9839893904},
             {'name':'rahul','phone':9234982449},
             {'name':'rahul','phone':9234982449},
             {'name':'rahul','phone':9234982449},
             {'name':'rahul','phone':9234982449}
        )
       
        
    }
    return render(request,"info.html",data)
def resources(request):
    return HttpResponse("welcom to bharatbuilds resources")

def resourcedetails(request,resourcesid):
    return HttpResponse(resourcesid)

def evodd(request):
    e=' '
    try:
        if request.method=='POST':
            if request.POST.get("num1")=="":
                    return render(request,'evodd.html',{'error':True})

            n1=int(request.POST.get("num1"))
            if n1 % 2==0:
                e=(f"{n1} is even number")
            else:
                e=(f"{n1} is odd number")
    except:
        e= 'invalid syntax'

        print(e)

    return render(request,'evodd.html',{'e':e})

def marksheet(request):
    if request.method == "POST":
        s1=eval(request.POST.get('subject1'))
        s2=eval(request.POST.get('subject2'))
        s3=eval(request.POST.get('subject3'))
        s4=eval(request.POST.get('subject4'))
        s5=eval(request.POST.get('subject5'))
        t= s1+s2+s3+s4+s5
        p=t*100/500
        if p>60:
            d="First Division"
        elif p>50:
            d="Second Division"
        elif p>40:
            d="Third Division"
        elif p<40:
            d="Fail"

        data={
            'total':t,
            'percentage':p,
            'div':d
        }

        return render(request,"marksheet.html",data)

