from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from systerm import models
# Register your models here.
from django.utils.translation import gettext, gettext_lazy as _


class UserProfileAdmin(UserAdmin):
    #重写fieldsets在admin后台加入自己新增的字段
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'department', 'position', 'superior', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Roles'), {'fields': ('roles',)}),
    )

admin.site.register(models.UserProfile, UserProfileAdmin)
# admin.site.register(models.UserProfile)
admin.site.register(models.Permission)
admin.site.register(models.Organization)
admin.site.register(models.Role)
admin.site.register(models.Menu)

