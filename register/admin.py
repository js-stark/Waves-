from django.contrib import admin
from .models import Register,RegisterItem

# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('register_id','date_added')

class RegisterItemAdmin(admin.ModelAdmin):
    list_diplay = ('event','register','is_active')

admin.site.register(Register,RegisterAdmin)
admin.site.register(RegisterItem,RegisterItemAdmin)

