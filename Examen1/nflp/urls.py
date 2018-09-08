from django.urls import path
from nflp import views


urlpatterns = [
	path('list_player/', views.List_Player.as_view(), name="List_Player_view"),
	path('list_team/', views.List_Team.as_view(), name="List_Team_view"),
	path('list_stadium/', views.List_Stadium.as_view(), name="List_Stadium_view"),
	path('detail_player/<int:pk>/', views.Detail_Player.as_view(), name="Detail_Player_view"),
	path('detail_team/<int:pk>/', views.Detail_Team.as_view(), name="Detail_Team_view"),
	path('detail_stadium/<int:pk>/', views.Detail_Stadium.as_view(), name="Detail_Stadium_view"),
	# path('update_tweet/<int:pk>/', views.Update_Tweet.as_view(), name="Update_Tweet_view"),
	# path('create_tweet/', views.Create_Tweet.as_view(), name="Create_Tweet_view"),
	# path('delete_tweet/<int:pk>/', views.Delete_Tweet.as_view(), name="Delete_Tweet_view"),
	

	# path('create_tweet2/', views.create_tweet, name="Create_Tweet_view"),


] 
