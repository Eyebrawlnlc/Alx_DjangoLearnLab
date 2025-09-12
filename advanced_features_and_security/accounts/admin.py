from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Article

class CustomUserAdmin(UserAdmin):
    """
    Admin configuration for CustomUser
    """
    model = CustomUser

    # Add the extra fields to fields shown in admin user change page
    fieldsets = UserAdmin.fieldsets + (
        ( 'Extra Info', {'fields': ('date_of_birth', 'profile_photo')} ),
    )

    # Also for adding user via admin interface
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Info', {'fields': ('date_of_birth', 'profile_photo')} ),
    )

    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_of_birth')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

# Also register Article so you can manage using groups / permissions
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author__username', 'author__email')
