from __future__ import unicode_literals
from django.db import models
from datetime import date
import re

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

class ShowManager(models.Manager):
    def form_validator(self, postData):
        errors = {}
        #Titlo del item
        if len(postData['titleInput']) < 3:
            errors['titleInput'] = "El Titulo debe tener al menos 3 caracteres"
        if Item.objects.filter(title=postData['titleInput']).exists():
            if postData['is_edit'] == 'no':
                errors['titleInput'] = "El Item Ya Existe!!"
        #Descripcion del item
        if len(postData['descriptionInput']) != 0:
            if len(postData['descriptionInput']) < 3:
                errors['descriptionInput'] = "La Descripcion debe tener al menos 3 caracteres"
        
        return errors

class User(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Item(models.Model):
    title = models.CharField(max_length=50)
    wisher = models.CharField(max_length=50)
    likes = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
