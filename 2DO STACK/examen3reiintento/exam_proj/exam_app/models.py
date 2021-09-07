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

class ItemManager(models.Manager):
    def item_validator(self, postData):
        errors = {}
        #titulo
        if len(postData['title']) < 3:
            errors['title'] = "No vale el titulo. el titulo debe tener mas de 3 caracteres"
        #titulo del item
        if len(postData['titleInput']) < 2:
            errors['titleInput'] = "El Titulo debe tener al menos 2 caracteres"
        if Item.objects.filter(title=postData['titleInput']).exists():
            if postData['is_edit'] == 'no':
                errors['titleInput'] = "El titulo Existe!!"
        #wisher
        if len(postData['wisherInput']) < 3:
            errors['wisherInput'] = "El deseo de tener al menos 3 caracteres"
        #descripcion
        if len(postData['descriptionInput']) != 0:
            if len(postData['descriptionInput']) < 3:
                errors['descriptionInput'] = "La Descripcion debe tener mas de 3 caracteres"

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

class Item(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    added_date = models.DateField()
    granted_date = models.DateField()
    likes = models.CharField(max_length=50)
    wisher = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()
