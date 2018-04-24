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
        return redirect(reverse('home'))
    else:
        passFlag = False
        return redirect(reverse('main'))

def login(request):
    if User.userManager.UserExistsLogin(request.POST, request):
        passFlag = True 
        user1 = User.objects.get(email=request.POST['email'])
        request.session['user'] = user1.id
        return redirect(reverse('home'))
    else:
        passFlag = False
        return redirect(reverse('main'))

def home(request):
    if "user" not in request.session:
        return redirect(reverse('main'))
    else:
        user_id = request.session['user']
        current_user = User.objects.get(id=user_id)
        quote_list = Quotable.objects.all()
        excluded = quote_list.exclude(favorited_by = user_id)
        favorites = current_user.favorites.all()
        context = {
            'name': current_user.name,
            'quotable_quotes': excluded,
            'your_favorites': favorites,
        }
        return render(request, "home.html", context)

def add_quote(request):
    user_id = request.session['user']
    current_user = User.objects.get(id=user_id)
    Quotable.objects.create(Quote=request.POST['Quote'],quoted_by=request.POST['quoted_by'],posted_by=current_user)
    return redirect(reverse('home'))


def add_favorite(request,id):
    user_id = request.session['user']
    current_user = User.objects.get(id=user_id)
    new_favorite = Quotable.objects.get(id = id)
    current_user.favorites.add(new_favorite)
    return redirect(reverse('home'))

def remove_favorite(request, id):
    user_id = request.session['user']
    current_user = User.objects.get(id=user_id)
    old_favorite = Quotable.objects.get(id = id)
    current_user.favorites.remove(old_favorite)
    return redirect(reverse('home'))


def profile(request, id):
    user_id = request.session['user']
    current_user = User.objects.get(id=user_id)
    other_user = User.objects.get(id = id)
    their_quotes = Quotable.objects.all()
    all_quotes = their_quotes.filter(posted_by = other_user)
    context = {
            'name': other_user.name,
            'count': other_user.posted_quotes.count(),
            'their_quotes': all_quotes
        }
    return render(request, "viewprofile.html", context)


def logout(request):
    del request.session['user'] 
    return HttpResponse("You are logged out.")

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
