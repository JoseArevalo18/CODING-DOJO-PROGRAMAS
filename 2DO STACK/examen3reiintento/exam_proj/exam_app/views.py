import re
from django.http import request
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Group, Item, Member, Review, User
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
    return redirect("/")

#4
def logout(request):
    request.session.flush()
    return redirect('/')

#5
def user_page(request, user_id):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or please log in first")
        return redirect('/')
    user = User.objects.get(id=user_id)

    context = {
        'one_user': user
    }
    return render(request, 'user_page.html', context)

#6
def create_group(request):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or please log in first")
        return redirect('/')
    if request.method == "POST":
        item_errors = Item.objects.item_validator(request.POST)
        errors = list(item_errors.values())

        if request.POST['author_dropdown'] == "-1":
            if request.POST['title'] == "":
                messages.error(request, "Please choose an author from the dropdown or create a new one")
            else:
                    author_errors = Item.objects.author_validator(request.POST)
                    errors += list(author_errors.values())

        if errors:
                for error in errors:
                    messages.error(request, error)
                return redirect ('/wishes/group_form')

        if request.POST['author_dropdown'] == "-1":
            author = Item.objects.create(title = request.POST['title'])
        else:
            author = Item.objects.get(id = request.POST['author_dropdown'])

        this_item = Item.objects.create(title = request.POST['title'])
        user = User.objects.get(id = request.session['logged_user'])
        this_item.add(author)
        return redirect('/user/dashboard')

#7
def group_form(request):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or please log in first")
        return redirect('/')

    context = {
        'authors': Item.objects.all()
    }
    return render(request, 'add_group.html', context)

#8
def show_group(request, group_id):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or please log in first")
        return redirect('/')
    context = {
        'item' : Item.objects.get(id=group_id)
    }
    return render(request, 'one_group.html', context)

#9
def add_review(request):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or please log in first")
        return redirect('/')

    if request.method == "POST":
        group = Item.objects.get(id=request.POST['group_reviewed'])
        errors = Review.objects.review_validator[request.POST]

        if errors:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect(f'/group/{group.id}')

        user = User.objects.get(id=request.session['logged_user'])
        return redirect(f'/group/{group.id}')

#10
def delete_review(request, review_id):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or please log in first")
        return redirect('/')
    review = Review.objects.get(id=review_id)
    review.delete()
    return redirect(f'/group/{review.group_reviewed.id}')
