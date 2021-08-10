from django.db import models

# Create your models here.



class Team(models.Model):

    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        db_table = 'team__fifa'

    def __str__(self):
        return str(self.name)


class Player(models.Model):

    class Position(models.TextChoices):
        RIGHT_WING = 'RW'
        CEMTRAL_ATTACKING_MIDFIELDER = 'CAM'
        LEFT_WING = 'LW'
        #FORWARDS
        STRIKER = 'ST' 
        CENTRE_FORWARD = 'CF'
        GOALKEEPER = 'GK'
        #DEFENDERS
        CENTER_BACK = 'CB'
        RIGHT_BACK = 'RB'
        LEFT_BACK =  'LB'
        LEFT_MIDFIELDER = 'LM'

        SWEEPER = 'SW'
        RIGHT_WING_BACK = 'RWB'
        LEFT_WING_BACK = 'LWB'
        CENTER_MIDFIELDER = 'CM'
        #MIDFIELDERS
        RIGHT_MIDFIELDER = 'RM'
        CENTRAL_DEFENSIVE_MIDFIELDER = 'CDM'
        LEFT_FORWARD = 'LF'
        LEFT_HALF = 'LH'

        NONE = 'None'

    id_fifa = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=255)
    position_full = models.CharField(max_length=100)
    country = models.CharField(max_length=255)
    position = models.CharField(max_length=5,choices=Position.choices,default=Position.NONE,)

    team = models.ForeignKey(
        Team,
        related_name='players',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'player__fifa'

    def __str__(self):
        return f'{self.name} {self.id_fifa}'


