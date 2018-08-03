# Generated by Django 2.0.7 on 2018-08-03 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enron', '0020_staffemail_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailAddress', models.CharField(max_length=64)),
                ('isTrust', models.BooleanField(default=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enron.StaffName')),
            ],
        ),
        migrations.CreateModel(
            name='Aliasf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailAddress', models.CharField(max_length=64)),
                ('type', models.CharField(blank=True, default=None, max_length=16, null=True)),
                ('number', models.IntegerField(default=0)),
                ('isTrust', models.BooleanField(default=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enron.StaffName')),
            ],
        ),
        migrations.AlterField(
            model_name='staffemail',
            name='type',
            field=models.CharField(default='intrusted', max_length=16),
        ),
    ]