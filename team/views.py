from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from .models import Team,Team_members
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def team(request,waves_team=None):

    team = None
    team_members = None

    if waves_team !=None:
        team = get_object_or_404(Team,slug=waves_team)
        team_members = Team_members.objects.filter(team=team)
    else:
        team = 'Waves'
        team_members = Team_members.objects.all()

    context = {
        'team':team,
        'team_members' :team_members
    }

    return render(request,'team/team.html',context=context)
