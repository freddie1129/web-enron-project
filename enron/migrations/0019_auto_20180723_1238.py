# Generated by Django 2.0.7 on 2018-07-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enron', '0018_bccemailnew_ccemailnew_stacommunication'),
    ]

    operations = [
        migrations.AddField(
            model_name='stacommunication',
            name='bccNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stacommunication',
            name='ccNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stacommunication',
            name='toNumber',
            field=models.IntegerField(default=0),
        ),
    ]
