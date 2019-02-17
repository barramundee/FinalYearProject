from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView, LogoutView
import home.views as home_views

app_name = 'home'

urlpatterns = [

    path('', LoginView.as_view(), {'template_name': 'registration/login.html'}),
    path('home/', home_views.defaultpage, name="home"),
    path('login/', LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
    path('logout/', LogoutView.as_view(), {'template_name': 'registration/logged_out.html'}, name='logout'),
    path('register/', views.register, name='register'),
    path('homepage/', views.HomepageView.as_view(), name='homepage'),
    path('searchresults/', views.SearchResultsView.as_view(), name='searchresults'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.edit_profile, name='profile_edit'),
    path('teams/', views.TeamViews.as_view(), name='teams'),
    path('teamhome/', views.TeamHomeViews.as_view(), name='teamhome'),
    path('agilepicker/', views.AgilePickerView.as_view(), name='agilepicker'),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile),
    # url(r'teams/(?P<teamname>[a-zA-Z0-9]+)$', views.get_team_name),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
