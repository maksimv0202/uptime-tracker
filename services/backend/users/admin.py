from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'created', 'updated')
    search_fields = ('username', 'email')
    ordering = ('username',)
