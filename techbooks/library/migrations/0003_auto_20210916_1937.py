# Generated by Django 3.2.7 on 2021-09-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
