from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Menu
from .models import MenuCategory, Logger
from .models import Person


# Register your models here.

admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Logger)
# admin.site.register(Person)

# Unregister the User provided by admin
admin.site.unregister(User)


@admin.register(User)
class NewAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        
        if not is_superuser:
            form.base_fields['username'].disabled = True
            
        return form
    
    
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    search_fields = ("first_name__startswith",)