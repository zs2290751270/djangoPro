# Generated by Django 4.2 on 2023-05-24 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_remove_team_team_leader_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_member',
        ),
    ]
