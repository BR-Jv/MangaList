# Generated by Django 5.1 on 2024-09-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangalist', '0005_manga_categoria_alter_ilustrador_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manga',
            old_name='Categoria',
            new_name='categoria',
        ),
        migrations.AddField(
            model_name='manga',
            name='generos',
            field=models.ManyToManyField(related_name='genManga', to='mangalist.genero'),
        ),
    ]
