# Generated by Django 3.2 on 2021-06-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='book',
            name='imageURL',
            field=models.URLField(max_length=500),
        ),
    ]
