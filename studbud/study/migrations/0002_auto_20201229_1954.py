# Generated by Django 3.1.4 on 2020-12-30 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='academic_seriousness',
            field=models.IntegerField(choices=[(1, '1 Not so serious'), (2, '2'), (3, '3'), (4, '4'), (5, '5 Very serious student')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='collaborative',
            field=models.IntegerField(choices=[(1, '1 Prefer minimal talking'), (2, '2'), (3, '3'), (4, '4'), (5, '5 Very interactive')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='extroverted',
            field=models.IntegerField(choices=[(1, '1 Not extroverted'), (2, '2'), (3, '3'), (4, '4'), (5, '5 Very extroverted')], default=0),
        ),
    ]
