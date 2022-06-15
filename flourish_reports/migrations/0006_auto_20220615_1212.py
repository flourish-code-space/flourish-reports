# Generated by Django 3.1.4 on 2022-06-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flourish_reports', '0005_auto_20220615_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recruitmentstats',
            old_name='not_total_attempted',
            new_name='total_not_attempted',
        ),
        migrations.AddField(
            model_name='recruitmentstats',
            name='participants_to_call',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Participants to call again'),
        ),
        migrations.AddField(
            model_name='recruitmentstats',
            name='study_participants',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Total study participants'),
        ),
    ]
