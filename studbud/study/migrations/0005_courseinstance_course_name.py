# Generated by Django 3.1.4 on 2020-12-30 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_remove_courseinstance_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinstance',
            name='course_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
