from django.contrib.auth.models import User

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields

from api.models import Space, Content

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
		allowed_methods = ['get']

class SpaceResource(ModelResource):
	class Meta:
		queryset = Space.objects.all()
		resource_name = 'space'
		authorization = Authorization()

class ContentResource(ModelResource):
	created_by = fields.ForeignKey(UserResource, 'user')

	class Meta:
		queryset = Content.objects.all()
		resource_name = 'content'
		authorization = Authorization()