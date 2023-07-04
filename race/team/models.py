import uuid

from django.db import models


class Team(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team_name = models.CharField(unique=True, max_length=128, blank=False)
    team_group = models.CharField(max_length=128, blank=True)
    team_win = models.IntegerField(default=0, blank=False)
    team_lose = models.IntegerField(default=0, blank=False)
    team_desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation time')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='update time')

    class Meta:
        db_table = 'race_team'
