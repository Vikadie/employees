# Generated by Django 4.0.1 on 2022-01-27 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, default='NO NAME', max_length=40, null=True)),
                ('egn', models.CharField(max_length=10, unique=True, verbose_name='EGN')),
                ('job_title', models.IntegerField(choices=[(1, 'Software Developer'), (2, 'QA Eng'), (3, 'DevOps Specialist')])),
                ('company', models.CharField(choices=[('Soft-Uni', 'Soft-Uni'), ('Google', 'Google'), ('Audi', 'Audi')], max_length=8)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employees_app.department')),
            ],
            options={
                'ordering': ('company', '-first_name'),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='employees_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dead_line', models.DateField(blank=True, null=True)),
                ('employees', models.ManyToManyField(to='employees_app.Employee')),
            ],
        ),
    ]
