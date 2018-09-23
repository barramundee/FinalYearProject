from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import login, logout
import home.views as home_views

app_name = 'home'

urlpatterns = [
    path('', login, {'template_name': 'home/login.html'}),
    path('home/', home_views.defaultpage, name="home"),
    path('login/', login, {'template_name': 'home/login.html'}, name='login'),
    path('logout/', logout, {'template_name': 'home/logout.html'}, name='logout'),
    path('register/', views.register, name='register'),
    path('homepage/', views.HomepageView.as_view(), name='homepage'),
    path('searchresults/', views.SearchResultsView.as_view(), name='searchresults'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.edit_profile, name='profile_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
