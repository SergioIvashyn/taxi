from django.db import models
from django.contrib.auth.models import Group,User
from django.shortcuts import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import mark_safe

from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify
from time import time
from django.db import connection
from django.db.models import F

# Create your models here.
def gen_slug(s):
	new_slug = slugify(s, allow_unicode=True)
	return new_slug + '-' +str(int(time()))

# Create your models here.
class Colour(models.Model):
	title = models.CharField(max_length=150)

	def __str__(self):
		return self.title

class State(models.Model):
	title = models.CharField(max_length=150)

	def __str__(self):
		return self.title

class Car(models.Model):
	mark = models.CharField(max_length=150)
	state = models.ForeignKey(State,on_delete=models.CASCADE)
	colour = models.ForeignKey(Colour,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.mark

class Driver(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	phonenumber = PhoneNumberField(unique=True)
	car = models.OneToOneField(Car,on_delete=models.CASCADE)
	slug = models.SlugField(max_length=50,unique=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.user.username)
		super().save(*args, **kwargs)


	def get_absolute_url(self):
		return reverse('driver_detail_url',kwargs={'slug': self.slug})

	def get_update_url(self):
		return reverse('driver_update_url', kwargs={'slug':self.slug})

	def get_delete_url(self):
		return reverse('driver_delete_url', kwargs={'slug':self.slug})

	def __str__(self):
		return self.user.username



class Client(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	phonenumber = PhoneNumberField(unique=True)
	slug = models.SlugField(max_length=50,unique=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.user.username)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('client_detail_url',kwargs={'slug': self.slug})

	def get_update_url(self):
		return reverse('client_update_url', kwargs={'slug':self.slug})

	def get_delete_url(self):
		return reverse('client_delete_url', kwargs={'slug':self.slug})

	def __str__(self):
		return self.user.username

class Status(models.Model):
	title = models.CharField(max_length=150,unique=True)

	def __str__(self):
		return self.title

class Order(models.Model):
	client = models.OneToOneField(Client,on_delete=models.CASCADE)
	driver = models.OneToOneField(Driver,on_delete=models.CASCADE,null=True,blank=True)
	place_from = models.CharField(max_length=150)
	status = models.ForeignKey(Status,on_delete=models.CASCADE)
	place_to = models.CharField(max_length=150)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.id)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('order_detail_url',kwargs={'slug': self.slug})

	def get_update_url(self):
		return reverse('order_update_url', kwargs={'slug':self.slug})

	def get_delete_url(self):
		return reverse('order_delete_url', kwargs={'slug':self.slug})

	def __str__(self):
		return str(self.id)	



class Operator(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	phonenumber = PhoneNumberField(unique=True)
	slug = models.SlugField(max_length=50,unique=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.user.username)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('operator_detail_url',kwargs={'slug': self.slug})

	def get_update_url(self):
		return reverse('operator_update_url', kwargs={'slug':self.slug})

	def get_delete_url(self):
		return reverse('operator_delete_url', kwargs={'slug':self.slug})

	def __str__(self):
		return self.user.username