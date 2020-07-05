# Generated by Django 2.2.14 on 2020-07-04 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Qbank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=500)),
                ('option1', models.CharField(blank=True, max_length=100)),
                ('option2', models.CharField(blank=True, max_length=100)),
                ('option3', models.CharField(blank=True, max_length=100)),
                ('option4', models.CharField(blank=True, max_length=100)),
                ('correctoption', models.IntegerField()),
                ('questionpaper', models.ManyToManyField(to='bank.QuestionPaper')),
            ],
        ),
    ]
