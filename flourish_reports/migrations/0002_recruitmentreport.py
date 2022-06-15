# Generated by Django 3.1.4 on 2022-06-15 07:34

import _socket
from django.db import migrations, models
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.utils


class Migration(migrations.Migration):

    dependencies = [
        ('flourish_reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitmentReport',
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
                ('study', models.CharField(blank=True, max_length=36, null=True, unique=True, verbose_name='Previous Studies')),
                ('dataset_total', models.PositiveIntegerField(blank=True, null=True, verbose_name='Dataset Totals')),
                ('expected_locator', models.PositiveIntegerField(blank=True, null=True, verbose_name='Expected Locator')),
                ('existing_locator', models.PositiveIntegerField(blank=True, null=True, verbose_name='Existing Locator')),
                ('missing_locator', models.PositiveIntegerField(blank=True, null=True, verbose_name='Missing Locator')),
                ('missing_worklist', models.PositiveIntegerField(blank=True, null=True, verbose_name='Missing On Worklist')),
                ('randomised', models.PositiveIntegerField(blank=True, null=True, verbose_name='Randomised')),
                ('total_attempts', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total Attempts')),
                ('not_total_attempted', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total Not Attempted')),
                ('continued_contact', models.PositiveIntegerField(blank=True, null=True, verbose_name='Continued Contact')),
                ('not_reacheble', models.PositiveIntegerField(blank=True, null=True, verbose_name='Not Reacheble')),
                ('declined', models.PositiveIntegerField(blank=True, null=True, verbose_name='Declined')),
                ('consented', models.PositiveIntegerField(blank=True, null=True, verbose_name='Consented')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
