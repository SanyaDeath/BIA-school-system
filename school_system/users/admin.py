from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import Student, User

admin.site.site_header = 'BIA SCHOOL SYSTEM'


class UserAdmin(DjangoUserAdmin):
    model = User
    fieldsets = DjangoUserAdmin.fieldsets + ((None, {
        'fields': ('role', 'middle_name',
                   'birth_date')}),)
    list_display = ('role', 'last_name', 'first_name', 'middle_name',
                    'birth_date', 'is_staff')

    def save_model(self, request, obj, form, change):
        if request.user.is_teacher:
            obj.is_staff = True
            obj.save()


admin.site.register(User, UserAdmin)


class StudentUser(UserAdmin):
    model = Student
    fieldsets = UserAdmin.fieldsets + ((None, {
        'fields': ('entry_year', 'klass')}),)
    list_display = ('role', 'last_name', 'first_name',
                    'middle_name', 'birth_date',
                    'entry_year', 'klass', 'is_staff')
    search_fields = ('last_name', 'first_name',
                     'middle_name', 'entry_year', 'klass')


admin.site.register(Student, StudentUser)
