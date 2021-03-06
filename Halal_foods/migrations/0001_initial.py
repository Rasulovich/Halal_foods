# Generated by Django 3.2.4 on 2021-06-07 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nums', models.IntegerField()),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('group', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField(max_length=50)),
                ('photo', models.ImageField(upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Halal_foods.category')),
            ],
        ),
    ]
