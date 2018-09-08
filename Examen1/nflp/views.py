from django.shortcuts import render
from nflp.models import Player,Team,Stadium
from django.views import generic
# Create your views here.
class List_Player(generic.ListView):
	template_name = "nflp/list_player.html"
	queryset = Player.objects.all()

class List_Team(generic.ListView):
	template_name = "nflp/list_teams.html"
	queryset = Team.objects.all()

class List_Stadium(generic.ListView):
	template_name = "nflp/list_stadiums.html"
	queryset = Stadium.objects.all()

class Detail_Player(generic.DetailView):
	template_name = "nflp/detail_player.html"
	model = Player

class Detail_Team(generic.DetailView):
	template_name = "nflp/detail_team.html"
	model = Team

class Detail_Stadium(generic.DetailView):
	template_name = "nflp/detail_stadium.html"
	model = Stadium