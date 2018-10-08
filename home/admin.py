from django.contrib import admin
from home.models import Profile, Tasks, NewsFeed

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'name', 'bio'
    )

    list_filter = ('user', 'name', 'bio')
    search_fields = ('user', 'bio')


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'profile', 'task', 'type', 'points', 'votes'
    )

class NewsFeedAdmin(admin.ModelAdmin):
    list_display = (
        'post_id',  'post', 'profile', 'created'
    )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tasks, TaskAdmin)
admin.site.register(NewsFeed, NewsFeedAdmin)
