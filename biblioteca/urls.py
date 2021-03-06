# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from biblioteca import views

urlpatterns = [
    url(r'^emprestimos?[/]$', views.emprestimos, name='emprestimos'),
    url(r'^bibliotecas?[/]$', views.bibliotecas, name='bibliotecas'),
    url(r'^cadastrar_pessoa_fisica/$', views.cadastrar_pessoa_fisica, name='cadastrar_pessoa_fisica'),
    url(r'^renovar_emprestimo/(?P<id>\d+)/$', views.renovar_emprestimo, name='renovar_emprestimo'),

    # url(r'^hello_world?[/]$', views.hello_world, name='hello_world'),
    # url(r'^somar_2/$', views.somar2, name='somar2'),
    # url(r'^somar/(?P<a>\d)/(?P<b>\d)/$', views.somar, name='somar'),
]
