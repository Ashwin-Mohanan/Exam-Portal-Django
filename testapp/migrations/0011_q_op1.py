# Generated by Django 4.0.2 on 2022-03-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0010_q_delete_ans'),
    ]

    operations = [
        migrations.AddField(
            model_name='q',
            name='op1',
            field=models.CharField(default='hidden', max_length=20),
        ),
    ]
