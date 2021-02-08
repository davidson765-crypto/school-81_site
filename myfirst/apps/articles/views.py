from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponse
from django.shortcuts import render , redirect
import random
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.transaction import atomic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from uson.models import Users
from datetime import datetime
from django.utils import formats
from django import forms
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
import smtplib # Use of SMTP is to connect to a mail server and send a message # Email Settings 


som = random.randrange(1, 1000000)

userr = ''

passwordd = ''

emaill = ''

last_namee = ''

statuss = ''

td_theme = '#383838'

th_theme = '#383838'

body_theme = '#474747'

button_theme = '#dcdcdc'

header_theme = '#2a2a2a'

main_theme = "Темная"

text_theme = '#b6c0bd'

button_text = "black"

        
    
def theme(request):
    
    global td_theme, th_theme, body_theme, button_theme, header_theme, text_theme, main_theme, button_text
    
    main_theme = request.POST.get("main_theme")
    
    if request.method=='POST':
        
        if main_theme=="Темная":
            
            td_theme = '#383838'
            
            body_theme = '#474747'
            
            th_theme = '#383838'
            
            button_theme = '#dcdcdc'
            
            header_theme = '#2a2a2a'
            
            text_theme = '#b6c0bd'
            
            main_theme = "Темная"
            
            button_text = "black"
            
        elif main_theme=="Facebook":
            
            td_theme = "#D0E8F2"
            
            th_theme = "#D0E8F2"
            
            body_theme = "#FCF8EC"
            
            button_theme = "#79A3B1"
            
            header_theme = "#79A3B1"
            
            text_theme = "black"
            
            main_theme = "Facebook"
            
            button_text = "black"
            
        elif main_theme=="ООО":
            
            td_theme = "#E6739F"

            th_theme = "#E6739F"
            
            body_theme = "#F1D4D4"
            
            button_theme = "#790C5A"
            
            header_theme = "#790C5A"
            
            text_theme = "white"
            
            main_theme = "ООО"
            
            button_text = "white"
            
            
        #elif main_theme=="Пустынная":
            
        
            
    
    return HttpResponseRedirect(reverse('articles:index'))



def confirm_mail(request):
    
    
    if request.method=='POST':
        
        code = request.POST.get('code')
        

        if code==str(som):
            
            
            if statuss=='Учитель':
            
                user = User.objects.create_user(username=userr,password=passwordd,email=emaill, last_name=last_namee)
            
                user = authenticate(request, username=userr, password=passwordd)
            
                user.is_staff = True
            
                user.save()
            
                login(request, user)

                return HttpResponseRedirect(reverse('articles:profile'))
                
                
            else:
                
                user = User.objects.create_user(username=userr,password=passwordd,email=emaill, last_name=last_namee)
            
                user = authenticate(request, username=userr, password=passwordd)
            
                user.is_staff = False
            
                user.save()
            
                login(request, user)

                return HttpResponseRedirect(reverse('articles:profile'))
                
            
        else:

            messages.error(request, '• код не верный')
            
            return render(request, 'articles/som.html', {'body_theme':body_theme, 'text_theme':text_theme, 'button_theme':button_theme, 'button_text':button_text})
            
    
    return render(request, 'articles/som.html', {'body_theme':body_theme, 'text_theme':text_theme, 'button_theme':button_theme, 'button_text':button_text})






def del_at(request):
    
    pep = request.POST.get('pep')
    
    mem = User.objects.get(username=request.user)
    
    mom = Users.objects.filter(mess_id=mem.id)
    
    mam = mom.values_list('messager', flat=True)
    
    
    if pep=='все' or pep=='всë' or pep=='all' or pep=='All' or pep=='Всë' or pep=='Все':
        
        mom.delete()
        
        return HttpResponseRedirect(reverse('articles:profile'))
    
    
    if pep not in mam:

        messages.error(request, '• достижение не найдено')
        
        return HttpResponseRedirect(reverse('articles:profile'))
        
        
    else:
    
        nom = mom.get(messager=pep)
    
        nom.delete()

        return HttpResponseRedirect(reverse('articles:profile'))
    
    
    


def other(request):
    
    
    if not request.user.is_staff:
    
        mess = User.objects.get(username=request.user)
    
        messager = request.POST.get('messager')
        
        messager_text = request.POST.get("messager_text")
        
        cp = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@#₽_&-+() /:!?;~`|•√π÷×¶∆£€$¢^°={\}%©®™℅][йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
        
        coplo = list(cp)
        
        nom = True
        
        ball = request.POST.get('ball')
        
        
        for i in coplo:
            
            
            if i in ball or ball=='':
                
                nom = False
                
                break
            
            
        if ball=='':
            
            messages.error(request, '• балл не может быть нулевым')

            return HttpResponseRedirect(reverse( 'articles:profile'))
        
            
        if nom==False:
            
            messages.error(request, '• баллы - это числа')
            
            return HttpResponseRedirect(reverse( 'articles:profile'))
            
            
        else:
            
            ball = int(ball)
            
            
            if ball>100:
                
                messages.error(request, '• самый высокий балл - 100')
                
                return HttpResponseRedirect(reverse('articles:profile'))
                
                
            else:
    
                mn = Users.objects.create(messager=messager, mess=mess, messager_text=messager_text, ball=ball)
    
                return HttpResponseRedirect(reverse( 'articles:profile')) 



def profile(request):
    
    
    if request.user.is_authenticated:
        
    
        first = None
    
        ok = True
    
        a = User.objects.get(username=request.user)
    
        b = Users.objects.filter(mess_id=a.id)
        
        maset = a.date_joined
        
        masot = formats.date_format(maset, "DATE_FORMAT")

        vist = list(b)
    
        ki = None
    
        sum_ball = 0
        
        for i in b:
            
            sum_ball+=i.ball
        
        
        a.first_name = sum_ball
        
        a.save()
        
        

        return render(request, 'articles/ishod.html', {'users': a, 'b': b, 'masot':masot, 'body_theme':body_theme, 'button_theme':button_theme,'text_theme':text_theme, 'td_theme':td_theme, 'button_text':button_text})
    
    
    else:
        
        return render(request, 'articles/ishod.html', {'body_theme':body_theme, 'button_theme':button_theme, 'text_theme':text_theme, 'td_theme':td_theme, 'button_text':button_text})

        

        


def index(request):
    
    list_count = User.objects.count()
    
    latest_articles_list = []
    
    latest=User.objects.all().order_by('-first_name')
    
    count_ball = []
    
    summa_ball = 0
    
    ball = None
    
    for i in range(10):
        
        
        if i==list_count:
            
            break
        
        
        latest_articles_list.append(latest[i])
        
        balls = Users.objects.filter(mess_id=latest[i].id)
        
        
        
        for i in balls:
            
            summa_ball += i.ball
            
            
        
        
    return render(request, 'articles/vika.html', { 'latest_articles_list':latest_articles_list, 'latest':latest, 'body_theme':body_theme, 'td_theme':td_theme, 'th_theme':th_theme, 'button_theme':button_theme, 'header_theme':header_theme, 'text_theme':text_theme, 'button_text':button_text})





@atomic
def detail(request, user_id):
    
    
    try:
        
        a=User.objects.get(id=user_id)
        
        
    except:
        
        messages.error(request, '• пользователь не найден')
        
        return HttpResponseRedirect(reverse('articles:index'))
    
    
    b = Users.objects.filter(mess_id=a.id)
    
    vist = list(b)
    
    first = None
    
    sum_ball = 0
    
    
    if len(vist)>1:
    
        first = vist[0]
            
        ki = []
            
            
        for i in vist:
            
            hk = i.ball
            
            ki.append(hk) 
                
            sum_ball = sum(ki)
            
    
        vist.remove(vist[0])
        
    
    return render(request, 'articles/detail.html', {'users': a, 'b': b, 'vist': vist, 'first': first, 'sum_ball': sum_ball, 'body_theme':body_theme, 'button_theme':button_theme, 'td_theme':td_theme, 'text_theme':text_theme, 'button_text':button_text}) 

    


def filt(request):
    
    abc = request.POST.get("ext")
    
    letters_list = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
    
    name_list = User.objects.values_list("username", flat=True)
    
    id_list = User.objects.values_list("id", flat=True)
    
    nam = True
    
    man = True
    
    
    for i in abc:
        
        
        if i in letters_list:
                
            nam = False
                
            break
            
        
        elif not i in letters_list:
            
            nam = True
            
            
    if nam==False:
        
        
        if abc in name_list:
            
            a = User.objects.get(username=abc)
        
            return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))
            
            
        else:
            
            messages.error(request, '• имя не найдено')
            
            return HttpResponseRedirect(reverse('articles:index'))
            
        
    elif nam==True:
        
        
        if int(abc) in id_list:
        
            a = User.objects.get(id=int(abc))
        
            return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))
            
            
        else:
            
            messages.error(request, '• id не найдено')
            
            return HttpResponseRedirect(reverse('articles:index'))



def log_in(request):
    
    all_us = User.objects.all()
    
    b = False
    
    
    if request.method=='POST':
        
        username = request.POST.get('username') 
        
        password = request.POST.get('password')
        
        
        for i in all_us:
            
            
            if i.username==username:
                
                b = True
                
                break


        if b==True:
         
            us = User.objects.get(username=username)
            
        
            if us.check_password(password):
                
                user = authenticate(request, username=username, password=password)
    
                login(request, user)
                
                return HttpResponseRedirect(reverse('articles:profile'))
                
            
            else:
                
                messages.error(request, "• пароль неверный")
                
          
        else:
        
            messages.error(request, '• имя не найдено')
       
    
    return render(request, 'articles/avt.html', {'body_theme':body_theme, 'button_theme':button_theme, 'text_theme':text_theme, 'button_text':button_text})
          
    
        
            


    

@login_required
def log_out(request):
    
    logout(request)
    
    return HttpResponseRedirect(reverse('articles:log_in'))
    
    
    
def signup(request):
    
    vak = "пожалуйста введите свою почту"
    
    ban = "почта должна содержать символ @ например: example@mail.ru"
    
    all_sig = User.objects.all()
    
    v = True
    
    b = False
    
    
    if request.method=='POST':
        
        global userr, passwordd, emaill, last_namee, statuss
        
        username = request.POST.get('username')
   
        email = request.POST.get('email')  
        
        last_name = request.POST.get('last_name')
    
        password = request.POST.get('password')
        
        password1 = request.POST.get('password1')
        
        
        for i in all_sig:
            
            if i.username==username:
                
                b = True
                
                break
        

        if b==False:
            
            p = list(password)
        
        
            if len(password)<8:
            
                messages.error(request, '• пароль должен содержать минимум 8 символов')

            
            else:
                
        
                if password==password1:
                    
                    reg = list('@#$_&-(*)/:;!~|•√π÷×¶∆£¢€¥^°={}\%©®™℅[]')
    

                    for i in range(len(p)):
                        
                        if p[i] in reg:
                
                            v = False
                            
                            break
                        
                
                    if v==True:
                    
                        status = request.POST.get('status')
                
                        molod = User.objects.values_list('email', flat=True)


                        if not email in molod:
                            
                            LOG_MAILTO = email
                            
                            LOG_PASS = 'Lopaknit247'
                            
                            LOG_FROM = 'ttset243@gmail.com'
                            
                            LOG_SUBJ = 'My school faculty'
                            
                            body = str(som)
                            
                            msg = MIMEMultipart()
                            
                            msg.attach(MIMEText(body))
                            
                            msg['Subject'] = LOG_SUBJ
                            
                            msg['From'] = LOG_FROM
                            
                            msg['To'] = LOG_MAILTO
                            
                            server = smtplib.SMTP('smtp.gmail.com:587')
                            
                            server.starttls()
                            
                            server.login(LOG_FROM, LOG_PASS)
                            
                            server.sendmail(LOG_FROM, LOG_MAILTO, msg.as_string())
                            
                            server.quit()

                            userr = username
                            
                            emaill = email
                            
                            passwordd = password
                            
                            last_namee = last_name
                            
                            statuss = status
                            
                            return render(request, 'articles/som.html', {'body_theme':body_theme, 'button_theme':button_theme, 'button_text':button_text})

                    
                        else:
                            
                            messages.error(request, '• такая почта уже зарегистрирована')
                            
                    
                    else:
                        
                        messages.error(request, '• пароль содержит не допустимые символы')
                        
        
                else:
                
                    messages.error(request, "• пароли не совпадают")

        
        else:
            
            messages.error(request, '• это имя существует')
        

    return render(request, 'articles/signup.html', {'vak': vak, 'ban': ban, 'body_theme':body_theme, 'button_theme':button_theme, 'text_theme':text_theme, 'button_text':button_text})
    



    


