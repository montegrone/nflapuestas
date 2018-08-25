# Generated by Django 2.1 on 2018-08-25 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nfl.Equipo')),
                ('visitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relacion1', to='nfl.Equipo')),
            ],
        ),
    ]
