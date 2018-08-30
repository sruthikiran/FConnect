from django.contrib import admin

# Register your models here.

from .models import College,UserProfileInfo,Resource,FAFSADeadline,Checklist

admin.site.register(College)
admin.site.register(UserProfileInfo)
admin.site.register(Resource)
admin.site.register(FAFSADeadline)
admin.site.register(Checklist)
