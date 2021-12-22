from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import User

admin.site.site_header = 'BIA SCHOOL SYSTEM'


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class UserAdmin(DjangoUserAdmin):
    form = MyUserChangeForm
    fieldsets = DjangoUserAdmin.fieldsets + ((None, {
        'fields': ('role', 'middle_name',
                   'birth_date', 'entry_year', 'klass')}),)
    list_display = ('role', 'last_name', 'first_name', 'middle_name',
                    'birth_date', 'entry_year', 'klass')


admin.site.register(User, UserAdmin)
