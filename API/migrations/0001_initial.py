# Generated by Django 4.1.1 on 2022-09-27 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('edad', models.IntegerField()),
            ],
            options={
                'db_table': 'personas',
                'managed': False,
            },
        ),
    ]