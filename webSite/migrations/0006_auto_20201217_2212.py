# Generated by Django 3.1.4 on 2020-12-17 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webSite', '0005_auto_20201217_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='chefsection',
            name='section',
            field=models.CharField(choices=[('électricité', 'électricité'), ('hydrolique', 'hydrolique'), ('mécanique', 'mécanique')], max_length=50, null='true'),
            preserve_default='true',
        ),
        migrations.AlterField(
            model_name='chefsection',
            name='nom',
            field=models.CharField(max_length=50, null='true'),
        ),
    ]