# Generated by Django 4.0.3 on 2022-08-31 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='body',
            new_name='description',
        ),
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
