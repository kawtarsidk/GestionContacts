from django.db import models
from __future__ import unicode_literals

# Create your models here.

# contact model

class Contact (models.Model):
    nom = models.CharField(max_lengh=100)
    adresse = models.CharField(max_lengh=250)
    ville = models.CharField(max_lengh=100)
    telephone = models.IntegerField()
    email = models.EmailField(max_length=200)
    profession = models.CharField(max_lengh=100)
    fk_categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE) """fk remplace onetomany"""
    fk_user = models.ForeignKey('User', on_delete=models.CASCADE) """fk remplace onetomany"""

    def __str__(self):
        self.email

class User(models.Model):

    nom = models.CharField(max_lengh=100)
    login = models.EmailField(max_length=200)
    password = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        self.login

class Categorie(models.Model)

    nom = models.CharField(max_lengh=100)

    def __str__(self):
        self.nom

