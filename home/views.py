from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import redirect
from .models import (User, Profile, Tasks, Teams, NewsFeed)
from django.template.response import TemplateResponse
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, RedirectView, TemplateView,
                                  UpdateView)
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from home.forms import Registration, EditProfile
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.


def homepage(request):
    return render(request, 'home/homepage.html')

class AgilePickerView(TemplateView):
    template_name = 'home/agile_picker.html'

    # def get(self, request):
    #     teams = Teams.objects.all()
    #     args = {'teams': teams}
    #     return render(request, 'home/agilepicker.html', args)

    @requires_csrf_token
    def my_view(request):
        c = {}
        # ...
        return render(request, 'home/agile_picker.html', c)

class HomepageView(TemplateView):
    template_name = 'home/homepage.html'
    model = Profile

    def profilehomepage(self, request):
        args = {'user': request.user}
        return render(request, 'home/homepage.html', args)

    def post(self, request):
        p = request.POST
        action = request.POST.get('action', '')

        if action == 'post':
            NewsFeed.objects.create(post=p['post'], profile=p['profile'])
            return render(request, 'home/homepage.html')


    def get(self, request):
        newsfeed = NewsFeed.objects.all()
        args = {'NewsFeed': newsfeed}
        return render(request, 'home/homepage.html', args)

    @requires_csrf_token
    def my_view(request):
        c = {}
        # ...
        return render(request, 'home/homepage.html', c)


class SearchResultsView(TemplateView):
    template_name = 'home/searchresults.html'


class TeamViews(TemplateView):
    template_name = 'home/teams.html'

    def get(self, request):
        teams = Teams.objects.all()
        args = {'teams': teams}
        return render(request, 'home/teams.html', args)

    @requires_csrf_token
    def my_view(request):
        c = {}
        # ...
        return render(request, 'home/teams.html', c)


class TeamHomeViews(TemplateView):
    template_name = 'home/teamhome.html'

    def get(self, request):
        teams = Teams.objects.all()
        args = {'teams': teams}
        return render(request, 'home/teamhome.html', args)

    @requires_csrf_token
    def my_view(request):
        c = {}
        # ...
        return render(request, 'home/teamhome.html', c)


class ProfileView(TemplateView):
    template_name = 'home/profile.html'
    model = Profile

    def profile(self, request):
        args = {'user': request.user}
        return render(request, 'home/profile.html', args)

    def post(self, request):
        p = request.POST
        action = request.POST.get('action', '')

        if action == 'create':
            Tasks.objects.create(profile=p['profile'], username=p['user'], task=p['task'], type="todo", points=p['points'])
            return render(request, 'home/profile.html')

        if action == 'thumbsup':
            r = request.POST
            vote = Tasks.objects.get(task=r['comment'])
            vote.votes += 1
            vote.save()
            return render(request, 'home/profile.html')

        if action == 'thumbsdown':
            r = request.POST
            vote = Tasks.objects.get(task=r['comment'])
            vote.votes -= 1
            vote.save()
            return render(request, 'home/profile.html')

        if action == 'delete':
            r = request.POST
            vote = Tasks.objects.get(task=r['comment'], username=r['user'], points=r['points'])
            vote.delete()

            return render(request, 'home/profile.html')

        if action == 'complete':
            r = request.POST
            vote = Tasks.objects.get(task=r['comment'])
            Tasks.objects.create(task=r['comment'], type="completed", username=r['user'], profile=r['profile'], points=r['points'],
                                 votes=r['votes'])
            vote.delete()

            # User.Profile.completedtasks += 1
            completed = Profile.objects.get(name=r['user'])
            completed.completedtasks += 1
            completed.save()

            return render(request, 'home/profile.html')

        if action == 'edit':
            r = request.POST
            vote = Tasks.objects.get(task=r['comment'])
            vote.task = r['newcomment']
            vote.save()

            return render(request, 'home/profile.html')

    def get(self, request):
        tasks = Tasks.objects.all()
        args = {'tasks': tasks}
        return render(request, 'home/profile.html', args)

    @requires_csrf_token
    def my_view(request):
        c = {}
        # ...
        return render(request, 'home/profile.html', c)


def edit_profile(request):
    model = Profile
    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
        form = EditProfile(instance=request.user.profile)
        args = {'form': form}

        return render(request, 'home/profile_edit.html', args)


# def create_task(request):
#     if request.method == "POST":
#         form = CreateTask(request.POST, instance=request.user.profile.task)
#
#         if form.is_valid():
#             form.save()
#             return redirect('/profile')
#
#     else:
#         form = CreateTask(instance=request.user.profile.task)
#         args = {'form': form}
#         return render(request, 'home/create_task.html', args)

def get_user_profile(request, username):
    user = User.objects.get(username=username)
    tasks = Tasks.objects.filter(username=username)
    return render(request, 'home/user_profile.html', {"user": user, "tasks": tasks})


def get_team_name(request, teamname):
    teamname = Teams.objects.get(teamname=teamname)
    return render(request, 'home/teamhome.html', {"team": teamname})


def defaultpage(request):
    return redirect('/homepage')


def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            HttpResponse("Congrats")
            return redirect('/login')

    else:
        HttpResponse("Congrats")
        form = Registration()
        args = {'form': form}
        return render(request, 'home/register.html', args)
