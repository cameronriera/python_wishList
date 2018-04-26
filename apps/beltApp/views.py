# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import *
from django.core.urlresolvers import reverse

def main(request):
    return render(request, "index.html")

def register(request):
    if User.userManager.isValidRegistration(request.POST, request):
        passFlag = True
        user1 = User.objects.get(email=request.POST['email'])
        request.session['user']= user1.id
        return redirect(reverse('dashboard'))
    else:
        passFlag = False
        return redirect(reverse('main'))

def login(request):
    if User.userManager.UserExistsLogin(request.POST, request):
        passFlag = True 
        user1 = User.objects.get(email=request.POST['email'])
        request.session['user'] = user1.id
        return redirect(reverse('dashboard'))
    else:
        passFlag = False
        return redirect(reverse('main'))

def dashboard(request):
    if "user" not in request.session:
        return redirect(reverse('main'))
    else:
        user_id = request.session['user']
        current_user = User.objects.get(id=user_id)
        wish_list = Product.objects.all()
        excluded = wish_list.exclude(favorited_by = user_id)
        favorites = current_user.favorites.all()
        context = {
            'name': current_user.name,
            'current_user': current_user,
            'other_products': excluded,
            'your_favorites': favorites,
        }
        return render(request, "dashboard.html", context)

def add_favorite(request,id):
    user_id = request.session['user']
    current_user = User.objects.get(id=user_id)
    new_favorite = Product.objects.get(id = id)
    current_user.favorites.add(new_favorite)
    return redirect(reverse('dashboard'))

def remove_favorite(request, id):
    user_id = request.session['user']
    current_user = User.objects.get(id=user_id)
    old_favorite = Product.objects.get(id = id)
    current_user.favorites.remove(old_favorite)
    return redirect(reverse('dashboard'))

def delete(request, id):
    user_id = request.session['user']
    current_user = User.objects.get(id=user_id)
    product = Product.objects.get(id = id)
    product.delete()
    return redirect(reverse('dashboard'))

def create(request):
    if "user" not in request.session:
        return redirect(reverse('main'))
    else:
        user_id = request.session['user']
        current_user = User.objects.get(id=user_id)
        return render(request, "create.html")

def add_product(request):
    user_id = request.session['user']
    current_user = User.objects.get(id=user_id)
    if len(request.POST['Item']) < 3:
        messages.warning(request, 'Item should be more than 3 characters.')
        return redirect(reverse('create'))
    else:        
        nuproduct = Product.objects.create(Item=request.POST['Item'], added_by = current_user)
        current_user.favorites.add(nuproduct)
        return redirect(reverse('dashboard'))

def view_product(request, id):
    if "user" not in request.session:
        return redirect(reverse('main'))
    else:
        user_id = request.session['user']
        current_user = User.objects.get(id=user_id)
        product = Product.objects.get(id = id)
        wish_list = product.favorited_by.all()
        context = {
                'item': product.Item,
                'wish_list': wish_list
            }
        return render(request, "viewproduct.html", context)


def logout(request):
    del request.session['user'] 
    return redirect(reverse('main'))

# def create(request):
#     title = request.POST['book_title']
    
#     if request.POST['new_author'] == '':
#         author= request.POST['new_author']
#     else:
#         author=request.POST['author_list']
#     book_one = Book.objects.create(title = title, author= author) 
#     print request.session.items()
#     Review.objects.create(review = request.POST['review'], rating = int(request.POST['rating']), book_id=book_one.id, user_id=request.session['user'])
#     return redirect('/books/'+ str(book_one.id))

# def profile(request, id):
