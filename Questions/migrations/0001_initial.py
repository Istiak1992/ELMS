# Generated by Django 3.1.6 on 2021-02-10 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_choice', models.CharField(max_length=1000)),
                ('second_choice', models.CharField(max_length=1000)),
                ('third_choice', models.CharField(max_length=1000)),
                ('fourth_choice', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('point', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('answer', models.CharField(max_length=1000)),
                ('Lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lessons.lesson')),
            ],
        ),
    ]