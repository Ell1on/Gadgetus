# Generated by Django 4.1.4 on 2023-01-27 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static/images/placeholder.png', null=True, upload_to=''),
        ),
    ]
