# Generated by Django 3.2.6 on 2021-09-13 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0004_livro_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='data_nasc',
            field=models.DateField(),
        ),
    ]
