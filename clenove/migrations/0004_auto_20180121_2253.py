# Generated by Django 2.0.1 on 2018-01-21 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clenove', '0003_auto_20180121_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clenove',
            name='motto',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Motto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clenove',
            name='patronci_zajmy',
            field=models.TextField(blank=True, default='', verbose_name='Patrončí zájmy'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clenove',
            name='pracovni_zkusenosti',
            field=models.TextField(blank=True, default='', verbose_name='Pracovní zkušenosti'),
            preserve_default=False,
        ),
    ]
