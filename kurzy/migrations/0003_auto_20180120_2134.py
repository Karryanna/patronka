# Generated by Django 2.0.1 on 2018-01-20 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurzy', '0002_auto_20180120_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='kurzy',
            name='anotace',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='kurzy',
            name='cena',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='kurzy',
            name='specifika',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='kurzy',
            name='vhodny_pro',
            field=models.TextField(null=True),
        ),
    ]
