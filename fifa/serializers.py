


from rest_framework import serializers
from .models import Player,Team


class PlayerSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField()

    class Meta:
        model = Player
        fields = ('id_fifa', 'name', 'position_full', 'country', 'position', 'team')


class TeamSerializer(serializers.ModelSerializer):    
    players = serializers.StringRelatedField(many=True)


    class Meta:

        model = Team
        fields = ('id', 'name', 'players')
