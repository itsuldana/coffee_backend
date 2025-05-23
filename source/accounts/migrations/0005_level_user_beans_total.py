# Generated by Django 4.2 on 2025-05-17 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_options_user_groups_user_user_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True, verbose_name='Уровень')),
                ('beans_required', models.PositiveIntegerField(verbose_name='Количество beans для достижения этого уровня')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='beans_total',
            field=models.IntegerField(default=0),
        ),
    ]
