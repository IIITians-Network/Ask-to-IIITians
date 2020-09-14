from django.shortcuts import render, redirect, get_object_or_404
from .forms import QueryForm, ReplyForm, DeleteForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Form
from django.core.mail import send_mail
import uuid 
from django.conf import settings

def home_view(request):

   
    object_list = Form.objects.all().order_by('-created')
    
    paginator = Paginator(object_list,5)
    page = request.GET.get('page')
    try:
        queries = paginator.page(page)
    except PageNotAnInteger:
        queries = paginator.page(1)
    except EmptyPage:
        queries = paginator.page(paginator.num_pages)

    return render(request, 'form/home.html', {'queries': queries})

def members_view(request):

    object_list = Form.objects.all().order_by('-created')
    
    paginator = Paginator(object_list,5)
    page = request.GET.get('page')
    try:
        queries = paginator.page(page)
    except PageNotAnInteger:
        queries = paginator.page(1)
    except EmptyPage:
        queries = paginator.page(paginator.num_pages)

    return render(request, 'form/member.html', {'queries': queries})






def reply_form(request, id):

    current_query = get_object_or_404(Form,pk=id)
    if request.method == "POST":
        
        reply_form = ReplyForm(instance=current_query, data=request.POST)
        if reply_form.is_valid():
            
            temp = reply_form.save(commit=False)
            current_question = temp
            name = current_question.name
            replied_by = current_question.replied_by
            email = current_question.email
           

            try:
                send_mail(
                'Question Replied',
                f'Dear {name} your question has been replied by {replied_by} please check on the site.',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
                )
                temp.secret_code = ''
                temp.replied = True
                temp.save()
            except:
                return render(request, 'form/error_email.html')


            return redirect('home')

    else:
        
        reply_form = ReplyForm()
    return render(request, 'form/reply_form.html', {'reply_form': reply_form})

def delete_form(request, id):

    current_query = get_object_or_404(Form,pk=id)
    if request.method == "POST":
        
        delete_form = DeleteForm(instance=current_query, data=request.POST)
        if delete_form.is_valid():
            current_query.delete()
            return redirect('home')

    else:
        
        delete_form = DeleteForm()
    return render(request, 'form/delete_form.html', {'delete_form': delete_form})


def form_view(request):

    if request.method == "POST":
        
        query_form = QueryForm(data=request.POST)
        if query_form.is_valid():
            current_question = query_form.save(commit=False)
            sec_code = uuid.uuid4().hex[:10].upper()
            name = current_question.name
            secret_code = sec_code
            institute = current_question.institute
            #get email of selected college
            college_email = get_email(institute)
            institute_name = get_institute(institute)
            question = current_question.query

    
            try:
                send_mail(
                    'Question Asked',
                    f'{name} has asked a question about {institute_name} please reply it. Here is your secret code {secret_code}\nHere is the Question="{question}"',
                    settings.EMAIL_HOST_USER,
                    [college_email],
                    fail_silently=False,
                )
                current_question.secret_code_value = sec_code
                current_question.save()

            except:
                return render(request, 'form/error_email.html')

            return redirect('home')

    else:
        
        query_form = QueryForm()
    return render(request, 'form/query_form.html', {'query_form': query_form})

# conver tuple to dict
def Convert(tup, di): 
    for a, b in tup: 
        di.setdefault(a, []).append(b) 
    return di 

def get_email(college):
    if college == 'general':
        return "iamaniiitian27@gmail.com"
    else:
        # print(f"----------------{college}-iiitians-network@googlegroups.com-------------------")
        return f"{college}-iiitiansnetwork@googlegroups.com"

def get_institute(college):
    institutes = [
        ('general', 'General'),
        ('kalyani','IIIT Kalyani'),
        ('guwhati','IIIT Guwhati'),
        ('bhagalpur','IIIT Bhagalpur'),
        ('bhopal', 'IIIT Bhopal'),
        ('dharwad', 'IIIT Dharwad'),
        ('gwalior', 'IIIT Gwalior'),
        ('jabalpur', 'IIIT Jabalpur'),
        ('kancheepuram', 'IIIT Kancheepuram'),
        ('kota', 'IIIT Kota'),
        ('kurnool', 'IIIT Kurnool'),
        ('lucknow', 'IIIT Lucknow'),
        ('nagpur', 'IIIT Nagpur'),
        ('pune', 'IIIT Pune'),
        ('raichur', 'IIIT Raichur'),
        ('ranchi', 'IIIT Ramchi'),
        ('sonepat', 'IIIT Sonepat'),
        ('sricity', 'IIIT Sricity'),
        ('surat', 'IIIT Surat'),
        ('tiruchirapalli', 'IIIT Tiruchirapalli'),
        ('una', 'IIIT Una'),
        ('vadodara', 'IIIT Vadodara'),
        ('kottayam', 'IIIT Kottayam'),
        ('manipur', 'IIIT Manipur'),
        ('agartala', 'IIIT Agartala'),
        ('allahabad', 'IIIT Allahabad')
    ]

    institutes = Convert(institutes, {})
    # print(f'-------------------------------------{institutes[college][0]}-----------------------------')

    return institutes[college][0]



