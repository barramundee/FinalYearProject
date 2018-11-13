from django.contrib import admin
from home.models import Profile, Tasks, NewsFeed, Teams

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

class TeamsAdmin(admin.ModelAdmin):
    list_display = (
        'teamname', 'agilemethodology'
    )

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tasks, TaskAdmin)
admin.site.register(NewsFeed, NewsFeedAdmin)
admin.site.register(Teams, TeamsAdmin)
