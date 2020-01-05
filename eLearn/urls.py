from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from .views import registration, home, admin, rotator, members, team, subscribers

app_name = 'eLearn'

urlpatterns = [
    path('', home.index, name='elearn.home'),
    path('register/', registration.newRegistration, name='elearn.newRegistration'),
    path('login/', registration.login, name='elearn.login'),
    path('admin/', admin.home, name='elearn.admin'),
    path('admin/saverotator/', rotator.saveRotator, name='elearn.saverotator'),
    path('admin/members/', members.editMembers, name='elearn.members'),
    path('admin/ourTeam/', team.editTeamMember, name='elearn.ourTeam'),
    path('admin/subscribers/', subscribers.editSubscribers, name='elearn.subscribers'),
]
