from django.contrib import admin
from gradebook.models import Grade,Utilizator
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UtilizatorInline(admin.StackedInline):
    model = Utilizator
    can_delete = False
    verbose_name_plural = "employee"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UtilizatorInline]

admin.site.register(Grade)
admin.site.register(Utilizator)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)