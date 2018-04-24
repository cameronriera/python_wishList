from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^main$', views.main, name ="main"),    
    url(r'^register$', views.register, name = "register"),
    url(r'^login$', views.login, name = "login"),    
    url(r'^ciao$', views.logout, name = "logout"),
    url(r'^quotes$', views.home, name = "home"),
    url(r'^quotes/add/(?P<id>\d+)$', views.add_favorite, name = "add"),
    url(r'^quotes/remove/(?P<id>\d+)$', views.remove_favorite, name = "remove"),
    url(r'^quotes/contribute$', views.add_quote, name = "add_quote"),
    url(r'^users/(?P<id>\d+)$', views.profile, name = "profile"),



    
    
    
    # url(r'^book/create$', views.create),
    # url(r'^books/(?P<id>\d+)$', views.profile),

    # url(r'^books$', views.books, name = "books"),
]