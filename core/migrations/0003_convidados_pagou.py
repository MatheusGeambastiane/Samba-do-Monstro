# Generated by Django 4.0.4 on 2022-06-01 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_convidados_options_convidados_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='convidados',
            name='pagou',
            field=models.BooleanField(default=False, help_text='Pagou o filha da puta ou deu uma de Yan?', verbose_name='Pagou?'),
        ),
    ]