from django.shortcuts import render
from nflp.models import Player 
from django.views import generic
# Create your views here.
class List_Player(generic.ListView):
	template_name = "nflp/list_player.html"
	queryset = Player.objects.all()