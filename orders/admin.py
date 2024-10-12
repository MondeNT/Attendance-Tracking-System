from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Employee
from .forms import AddEmployeeForm

# Custom admin class for the User model
class CustomUserAdmin(UserAdmin):
    add_form = AddEmployeeForm

    # Define the fields to be displayed in the list view in the admin interface
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active']
    list_filter = ['role', 'is_staff', 'is_active']

    # Define fields to be shown when adding a new User in the admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role', 'name', 'surname', 'phone', 'email', 'is_staff', 'is_active')}
        ),
    )

    # Define fields to be shown when editing an existing User
    fieldsets = (
        (None, {'fields': ('username', 'email', 'role', 'name', 'surname', 'phone', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}), 
    )

    search_fields = ['username', 'email']
    ordering = ['username']

# Register the User model using the custom admin interface
admin.site.register(User, CustomUserAdmin)

# Register the Employee model
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'surname', 'age', 'phone', 'gender', 'email']
    search_fields = ['name', 'surname', 'phone']
