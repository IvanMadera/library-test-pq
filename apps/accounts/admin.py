from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.forms import AdminPasswordChangeForm

# Register your models here.
from .models import User
from .forms import UserChangeForm, UserCreationForm

@admin.register(User)
class AdminUser(auth_admin.UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ( 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    limited_fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info', {
         'fields': ('first_name',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ('id', 'email', 'username', 'is_active', 'is_staff', 'is_superuser',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'username',)
    ordering = ('email',)
    readonly_fields = ('last_login', 'date_joined',)
