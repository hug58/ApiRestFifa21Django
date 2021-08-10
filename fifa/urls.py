from django.urls import path
from fifa.views import PlayersView,TeamView


urlpatterns = [
    path('players', PlayersView.as_view(), name="players_list"),
    path('team', TeamView.as_view(), name="team_list"),
]