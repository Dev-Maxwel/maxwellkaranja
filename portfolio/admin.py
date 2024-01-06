from django.contrib import admin
from .models import emailingInfo


class emailingInfoAdmin(admin.ModelAdmin):
    # display datetime in the changelist
    list_display = ('name', 'email', 'timeStamp')

admin.site.register(emailingInfo, emailingInfoAdmin)
