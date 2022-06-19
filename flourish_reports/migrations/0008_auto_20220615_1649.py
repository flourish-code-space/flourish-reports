# Generated by Django 3.1.4 on 2022-06-15 14:49

import _socket
from django.db import migrations, models
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.utils


class Migration(migrations.Migration):

    dependencies = [
        ('flourish_reports', '0007_remove_recruitmentstats_continued_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalRecruitmentStats',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('total_attempts', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total attempts')),
                ('not_attempted', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total not attempted')),
                ('total_participants_to_call_again', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total participants to call again')),
                ('total_participants_not_reachable', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total participants not reachable')),
                ('total_decline', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total decline')),
                ('total_consented', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total consented')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='recruitmentstats',
            name='not_reacheble',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Participant not reachable'),
        ),
    ]
