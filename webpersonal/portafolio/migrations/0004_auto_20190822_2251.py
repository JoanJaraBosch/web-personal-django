# Generated by Django 2.2.4 on 2019-08-22 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0003_project_moreinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Desccripció'),
        ),
    ]
