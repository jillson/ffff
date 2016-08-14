from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    espnID = models.CharField(max_length=40)
    name = models.CharField(max_length=128)

class Player(models.Model):
    espnID = models.CharField(max_length=40)
    name = models.CharField(max_length=128)

class Position(models.Model):
    name = models.CharField(max_length=128)
    abbr = models.CharField(max_length=4)
    
class PlayerInstance(models.Model):
    year = models.IntegerField()
    player = models.ForeignKey("Player")
    team = models.ForeignKey("Team")
    pos = models.ForeignKey("Position")

class WeekStats(models.Model):
    target = models.ForeignKey("PlayerInstance")
    weekNumber = models.IntegerField()
    rushingYards = models.IntegerField(default=0)
    rushingAttempts = models.IntegerField(default=0)
    rushingFumbles = models.IntegerField(default=0)
    rushingTDs = models.IntegerField(default=0)
    passingYards = models.IntegerField(default=0)
    passingAttempts = models.IntegerField(default=0)
    passingFumbles = models.IntegerField(default=0)
    passingTDs = models.IntegerField(default=0)
    throwingYards = models.IntegerField(default=0)
    throwingAttempts = models.IntegerField(default=0)
    throwingInterceptions = models.IntegerField(default=0)
    defenseSacks = models.IntegerField(default=0)
    defenseFumbles = models.IntegerField(default=0)
    defenseInterceptions = models.IntegerField(default=0)
    kickerFG = models.IntegerField(default=0)
    kickerPAT = models.IntegerField(default=0)
    
    

class PreviewStats(models.Model):
    target = models.ForeignKey("PlayerInstance")
    weekNumber = models.IntegerField()
    #startedPercent = 
    
class Human(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class HumanInstance(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey("Human")
    season = models.ForeignKey("Season")

class Season(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(default=2016)
    currentWeek = models.IntegerField(default=0)

class GameInstance(models.Model):
    season = models.ForeignKey("Season")
    weekNumber = models.IntegerField()
    homeTeam = models.ForeignKey("HumanInstance",related_name="homeGames")
    awayTeam = models.ForeignKey("HumanInstance",related_name="awayGames")
    homeScore = models.IntegerField(null=True)
    awayScore = models.IntegerField(null=True)
    
