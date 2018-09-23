from django.contrib import admin
from home.models import Profile, Tasks

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'bio'
    )

    list_filter = ('user', 'bio')
    search_fields = ('user', 'bio')


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'profile', 'task', 'type', 'points', 'votes'
    )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tasks, TaskAdmin)
