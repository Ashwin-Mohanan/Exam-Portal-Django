# Generated by Django 4.0.2 on 2022-03-19 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_q_qta4_q_qta5'),
    ]

    operations = [
        migrations.RenameField(
            model_name='q',
            old_name='Qta',
            new_name='Qta1',
        ),
        migrations.RenameField(
            model_name='q',
            old_name='QUESTION2',
            new_name='Qta2',
        ),
    ]