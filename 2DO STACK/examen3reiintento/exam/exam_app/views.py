from typing import ContextManager
from django.contrib import messages
from django.db.models.expressions import Value
from django.shortcuts import redirect, render
from .models import Item, User
import bcrypt
#0
# Create your views here.
def index(request):
    return render(request, 'index.html')
#1
#localhost:8000/user/create_user
def create_user(request):
    if request.method == "POST":
        # Validation check before safe in our DB
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/')

        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(hash_pw)
        new_user = User.objects.create(
            name = request.POST['name'],
            lastname = request.POST['lastname'],
            email = request.POST['email'],
            password = hash_pw
        )
        request.session['logged_user'] = new_user.id

        return redirect('/user/dashboard')
    return redirect("/")

#2
def dashboard(request):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or please log in first")
        return redirect('/')

    context = {
        'logged_user' : User.objects.get(id=request.session['logged_user']),
        'all_items' : Item.objects.order_by('-created_at')[:3]
    }
    return render(request, 'dashboard.html', context)

#3
def login(request):
    if request.method == "POST":
        user = User.objects.filter(email = request.POST['email'])
        if user:
            log_user = user [0]
            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                request.session['logged_user'] = log_user.id
                return redirect('/user/dashboard')
        messages.error(request, "Email/password are incorrect. Please retry")
    return redirect('/')

#4
def logout(request):
    request.session.flush()
    return redirect('/')

#5
def dashboard(request):
    return render(request, 'dashboard.html')
#6
def addShow(request):
    # errors = Item.objects.form_validator(request.POST)
    # if len(errors) > 0:
    #     for key, value in errors.items():
    #         messages.error(request,value)
    #     return redirect('/wish/new')
    # else:
        new_item = Item.objects.create(
                title = request.POST["titleInput"],
                wisher = request.POST["wisherInput"],
                release_date = request.POST["dateInput"],
                description = request.POST["descriptionInput"],
            )
        context = {
                'new_item' : new_item
            }
        return render(request, 'add_wishes.html',context)
#7
def displayShow(request):
    context = {
        'all_item' : Item.objects.all()
    }
    return render(request, 'dashboard.html',context)
#8
def showInfo(request,number):
    new_item = Item.objects.get(id=number)
    context = {
        'new_item' : new_item
    }
    return render(request, 'add_wishes.html',context)
#9
def editShow(request,number):
    if request.method == "POST":
        errors = Item.objects.form_validator(request.POST)
        if len(errors) > 0:
            edit_item = Item.objects.get(id=number)
            context = {
                    'new_item' : edit_item
            }
            for key, value in errors.items():
                messages.error(request,value)
            context['up_date']= str(context['new_item'].release_date)
            return render(request, 'edit_wishes.html',context)
        else:
            update_item = Item.objects.get(id=request.POST['show_id'])
            update_item.title = request.POST['titleInput']
            update_item.wisher = request.POST['wisherInput']
            update_item.release_date = request.POST['dateInput']
            update_item.description = request.POST['descriptionInput']
            update_item.save()
            context = {
                'new_item' : update_item
            }
            return render(request, 'add_wishes.html',context)
    edit_item = Item.objects.get(id=number)
    context = {
        'new_item' : edit_item
    }
    context['up_date']= str(context['new_item'].release_date)
    return render(request, 'edit_wishes.html',context)
#10
def delete_show(request,number):
    del_item = Item.objects.get(id=number)
    del_item.delete()
    return redirect('/wish/')
