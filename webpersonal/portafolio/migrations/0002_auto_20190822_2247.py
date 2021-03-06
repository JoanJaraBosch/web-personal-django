# Generated by Django 2.2.4 on 2019-08-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de creació'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Desccripció'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects', verbose_name='Imatge'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Títol'),
        ),
        migrations.AlterField(
            model_name='project',
            name='updatedDate',
            field=models.DateTimeField(auto_now=True, verbose_name='Data dactualització'),
        ),
    ]
