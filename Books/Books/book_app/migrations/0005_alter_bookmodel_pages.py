# Generated by Django 3.2.4 on 2021-06-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0004_alter_bookmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='pages',
            field=models.IntegerField(),
        ),
    ]
