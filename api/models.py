from django.db import models
from django.contrib.auth.models import User

class Space(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=200)
	description = models.TextField(blank=True,null=True)

	avatar = models.ImageField(upload_to='space_avatar/',blank=True,null=True)
	color = models.CharField(max_length=8,blank=True,null=True)

	# If true, anyone can enter and see the contents
	is_view_public: models.BooleanField(default=True)
	# If true, anyone can create content
	is_create_public: models.BooleanField(default=True)

	members = models.ManyToManyField(User,blank=True,null=True)

	# If the group is not public, anyone with the access_url can access it
	access_url: models.CharField(blank=True,null=True)

	created_by: models.ForeignKey(User,on_delete=models.SET_NULL)

	created_on: models.DateField(auto_now=False, auto_now_add=True)
	last_modified: models.DateField(auto_now=True, auto_now_add=False)
	deleted_on: models.DateField(blank=True,null=True)

class Content(models.Model):
	title: models.CharField(max_length=150)
	slug: models.SlugField(max_length=300)
	content: models.TextField(blank=True,null=True)

	related: models.ForeignKey('self', on_delete=models.SET_NULL,blank=True,null=True)

	url: models.URLField(blank=True,null=True)
	is_embed: models.BooleanField(blank=True,null=True)

	shortlink: models.CharField(max_length=50,blank=True,null=True)
	shortlink_deleted_on: models.DateField(blank=True,null=True)

	created_by: models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)

	created_on: models.DateField(auto_now=False, auto_now_add=True)
	last_modified: models.DateField(auto_now=True, auto_now_add=False)
	deleted_on: models.DateField(blank=True,null=True)
