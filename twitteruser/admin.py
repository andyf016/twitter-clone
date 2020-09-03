from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import CustomUser, FollowingUser

UserAdmin.fieldsets += ('Custom fields set', {'fields': ['bio', 'age', 'location', 'birthday']}),
admin.site.register(CustomUser, UserAdmin)
admin.site.register(FollowingUser)