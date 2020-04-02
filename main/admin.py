from django.contrib import admin

from .models import Account, Space, Content
# Register your models here.

admin.site.register(Account)
admin.site.register(Space)
admin.site.register(Content)