# Generated by Django 2.0.1 on 2018-01-21 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clenove', '0002_auto_20180121_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clenove',
            name='motto',
            field=models.CharField(max_length=200, null=True, verbose_name='Motto'),
        ),
        migrations.AlterField(
            model_name='clenove',
            name='patronci_zajmy',
            field=models.TextField(null=True, verbose_name='Patrončí zájmy'),
        ),
        migrations.AlterField(
            model_name='clenove',
            name='pracovni_zkusenosti',
            field=models.TextField(null=True, verbose_name='Pracovní zkušenosti'),
        ),
    ]