# Generated by Django 4.0.2 on 2022-04-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0015_java'),
    ]

    operations = [
        migrations.AlterField(
            model_name='java',
            name='Qta1',
            field=models.CharField(default='SOME STRING', max_length=500),
        ),
        migrations.AlterField(
            model_name='java',
            name='correctop',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='java',
            name='op1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='java',
            name='op2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='java',
            name='op3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='java',
            name='op4',
            field=models.CharField(default='', max_length=200),
        ),
    ]
