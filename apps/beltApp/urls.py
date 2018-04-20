from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^main$', views.main, name ="main"),    
    url(r'^login$', views.login, name = "login"),
    url(r'^register$', views.register, name = "register"),
    url(r'^friends$', views.friends, name = "friends"),
    url(r'^ciao$', views.logout, name = "logout"),
    # url(r'^books/add$', views.add, name = "add"),
    # url(r'^book/create$', views.create),
    # url(r'^books/(?P<id>\d+)$', views.profile),

    # url(r'^books$', views.books, name = "books"),
]