# Generated by Django 4.0.2 on 2022-03-08 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_q_qta3'),
    ]

    operations = [
        migrations.AddField(
            model_name='q',
            name='Qta4',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
        migrations.AddField(
            model_name='q',
            name='Qta5',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
    ]
