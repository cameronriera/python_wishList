from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^main$', views.main, name ="main"),    
    url(r'^register$', views.register, name = "register"),
    url(r'^login$', views.login, name = "login"),    
    url(r'^ciao$', views.logout, name = "logout"),
    url(r'^dashboard$', views.dashboard, name = "dashboard"),
    url(r'^wish_items/add/(?P<id>\d+)$', views.add_favorite, name = "add"),
    url(r'^wish_items/remove/(?P<id>\d+)$', views.remove_favorite, name = "remove"),
    url(r'^wish_items/delete/(?P<id>\d+)$', views.delete, name = "delete"),
    url(r'^wish_items/(?P<id>\d+)$', views.view_product, name = "view_product"),
    url(r'^wish_items/create$', views.create, name = "create"),
    url(r'^wish_items/create/new$', views.add_product, name = "add_product"),





    
    
    
    # url(r'^book/create$', views.create),
    # url(r'^books/(?P<id>\d+)$', views.profile),

    # url(r'^books$', views.books, name = "books"),
]