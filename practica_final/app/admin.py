from django.contrib import admin

# Register your models here.

from .models import Activitie,UsersPage,Publication

admin.site.register(Activitie)
admin.site.register(UsersPage)
admin.site.register(Publication)
