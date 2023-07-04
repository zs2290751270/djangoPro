import uuid
from django.db import models
from ..team.models import Team


class Member(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member_name = models.CharField(unique=True, max_length=128, blank=False)
    member_code = models.CharField(unique=True, max_length=128, blank=False)
    member_desc = models.TextField(blank=True)
    team_info = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='team',
        null=True
    )
    is_leader = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation time')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='update time')

    class Meta:
        db_table = 'race_member'

