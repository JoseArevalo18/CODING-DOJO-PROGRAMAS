from django.db import models
import re
from django.db.models.base import Model

# VALIDATIONS

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        # ALL THE VALIDATION FOR THE FORM
        errors = {}
        #nombre
        if len(postData['name']) < 2 and len(postData['name']) > 50:
            errors['name'] = "Invalid name. Name must be at least 3 characters"
        #segundo nombre
        if len(postData['lastname']) < 2:
            errors['lastname'] = "Invalid lastname. lastname must be at least 3 characters"
        #email
        if not EMAIL_REGEX.match(postData['email']):   
            errors['email'] = "Invalid email address!"
        #correo duplicado
        users_with_email = User.objects.filter(email = postData['email'])
        if len(users_with_email) >= 1:
            errors['duplicate'] = "Email already exists."
        #contraseña
        if len(postData['password']) < 5:
            errors['password'] = "Password must be at least 5 characters"
        if postData['password'] != postData['confirm_password']:
            errors['pw_match'] = "Password must match!"
        return errors       

class GroupManager(models.Manager):
    def group_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Invalid title. Title must be at least 3 characters"
        return errors 

class AuthorManager(models.Manager):
    def author_validator(self, postData):
        errors = {}
        if len(postData['member_name']) < 2 or len(postData['member_name']) > 50:
            errors['member_name'] = "Invalid name. Name must be at least 3 characters"
        member_in_db = Member.objects.filter(name=postData['member_name'])
        if len(member_in_db) >= 1:
            errors['duplicate'] = 'Member already exists.'
        return errors  

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}
        if len(postData['content']) < 2:
            errors['content'] = "Invalid content. Content must be at least 3 characters"
        return errors 



# MODELS CREATION
class User(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Group(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = GroupManager()

class Member(models.Model):
    name = models.CharField(max_length=75)
    group = models.ManyToManyField(Group, related_name="member")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

class Review(models.Model):
    content = models.TextField()
    persons = models.TextField()
    user_review = models.ForeignKey(User, related_name="user_reviews", on_delete=models.CASCADE)
    group_reviewed = models.ForeignKey(Group, related_name="group_reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()