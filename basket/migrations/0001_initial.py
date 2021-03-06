# Generated by Django 2.0.4 on 2018-04-20 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=0)),
                ('rut', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=200)),
                ('birthdate', models.DateField()),
                ('age', models.IntegerField(default=0)),
                ('rut', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=200)),
                ('weight', models.IntegerField(default=0)),
                ('photo', models.ImageField(upload_to='')),
                ('position', models.CharField(choices=[('BA', 'Base'), ('ES', 'Escolta'), ('AL', 'Alero'), ('AP', 'AlaPivot'), ('PI', 'Pivot')], default='BA', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('code', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.Team'),
        ),
    ]
