from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    # Specify the fields to be displayed in the user list view
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_active', 'date_joined', 'password')
    
    # Enable searching by username and email
    search_fields = ('username', 'email')
    
    # Set default ordering by username
    ordering = ('username',)
    
    # Add filtering options for user type and active status
    list_filter = ('user_type', 'is_active', )

    # Customize the fields in the admin form
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password', 'user_type', 'position')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined'),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'user_type')
            }
        ),
    )


# Customize the PerformanceReview admin
class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'date')
    search_fields = ('user__username', 'goals', 'feedback', )  
    list_filter = ('user__user_type', 'date', )

    def user_type(self, obj):
        return obj.user.user_type 

    user_type.admin_order_field = 'user__user_type' 
    user_type.short_description = 'User Type'  

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(PerformanceReview, PerformanceReviewAdmin)


