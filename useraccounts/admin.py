from django.contrib import admin
from useraccounts.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "contact", )