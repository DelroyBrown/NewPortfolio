from django.contrib import admin
from .models import WelcomePageVisitorName

class WelcomePageVisitorNameAdmin(admin.ModelAdmin):
    list_display = ('visitors_name', 'submit_time')

admin.site.register(WelcomePageVisitorName, WelcomePageVisitorNameAdmin)
