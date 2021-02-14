# Generated by Django 3.1.6 on 2021-02-10 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnswerChoice',
        ),
        migrations.AddField(
            model_name='question',
            name='first_choice',
            field=models.CharField(default='First Possible Answer', max_length=1000),
        ),
        migrations.AddField(
            model_name='question',
            name='fourth_choice',
            field=models.CharField(default='Fourth Possible Answer', max_length=1000),
        ),
        migrations.AddField(
            model_name='question',
            name='second_choice',
            field=models.CharField(default='Second Possible Answer', max_length=1000),
        ),
        migrations.AddField(
            model_name='question',
            name='third_choice',
            field=models.CharField(default='Third Possible Answer', max_length=1000),
        ),
    ]