# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import *

import bcrypt
import re
from django.contrib import messages

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def isValidRegistration(self, userInfo, request):
        passFlag = True
        if not userInfo['name'].isalpha():
            messages.warning(request, 'First name contains non-alpha characters.')
            passFlag = False
        if len(userInfo['name']) < 3:
            messages.warning(request, 'First name is too short.')
            passFlag = False
        if not userInfo['alias'].isalpha():
            messages.warning(request, 'Last name contains non-alpha characters.')
            passFlag = False
        if len(userInfo['alias']) < 3:
            messages.warning(request, 'Last name is too short.')
            passFlag = False
        if not EMAIL_REGEX.match(userInfo['email']):
            messages.warning(request, 'Email is not vaild!')
            passFlag = False
        if len(userInfo['password']) < 8:
            messages.warning(request, 'Password is too short.')
            passFlag = False
        if userInfo['password'] != userInfo['confirm_password']:
            messages.warning(request, "The passwords you've entered do not match.")
            passFlag = False
        if User.objects.filter(email = userInfo['email']):
			messages.error(request, "This email already exists in our database.")
			passFlag = False

        birthday = userInfo['DOB']
        today = date.today().strftime("%Y-%m-%d")
        if birthday >= today:
            messages.warning(request, "Birthday cannot be the present day or a future date.")
            passFlag = False

        if passFlag == True:
            messages.success(request, "Success! Welcome, " + userInfo['name'] + "!")
            hashed = bcrypt.hashpw(userInfo['password'].encode(), bcrypt.gensalt())
            User.objects.create(name = userInfo['name'], alias = userInfo['alias'], email = userInfo['email'], password = hashed, birthday = birthday)
        return passFlag

    def UserExistsLogin(self, userInfo, request):
        passFlag = True
        if User.objects.filter(email = userInfo['email']):
            hashed = User.objects.get(email = userInfo['email']).password
            hashed = hashed.encode('utf-8')
            password = userInfo['password']
            password = password.encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                messages.success(request, "Success! Welcome, " + User.objects.get(email = userInfo['email']).name + "!")
                passFlag = True
            else:
                messages.warning(request, "Unsuccessful login. Incorrect password")
                passFlag = False
        else:
            messages.warning(request, "Your email is either incorrect or not in our database.")
            passFlag = False
        return passFlag

class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
    objects = models.Manager()

class Product(models.Model):
    Item = models.CharField(max_length = 255)
    added_by = models.ForeignKey(User, related_name="added_products")
    favorited_by = models.ManyToManyField(User, related_name="favorites")
    date_added = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()
