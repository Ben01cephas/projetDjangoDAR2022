from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.urls import reverse
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    last_name = models.TextField(max_length=50)
    first_name = models.TextField(max_length=50)
    adresse = models.TextField(max_length=50)
    telephone = models.TextField(max_length=50)
    email = models.EmailField('email address', unique=True)
    is_fromEsmt = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    
    def get_update_url(self):
        return reverse('update',kwargs={'pk':self.id})

class Professeur(models.Model):
    id_prof = models.BigAutoField(primary_key=True)
    nom_prof = models.CharField(max_length=50)

class Filliere(models.Model):
    id_filliere = models.BigAutoField(primary_key=True)
    nom_filliere = models.CharField(max_length=50)   

class Epreuve(models.Model):
    id_epreuve = models.BigAutoField(primary_key=True)
    nom_fichier_epreuve = models.FileField(upload_to="files/epreuve/")
    nom_fichier_correction = models.FileField(upload_to="files/epreuve/")
    nom_epreuve = models.CharField(max_length=50)
    niveau_epreuve = models.CharField(max_length=50)
    annee_epreuve = models.IntegerField()
    matiere_epreuve = models.CharField(max_length=50)
    nom_prof = models.CharField(max_length=50)
    nom_filliere = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
        
class Test(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50)     