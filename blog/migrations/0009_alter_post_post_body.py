# Generated by Django 3.2.12 on 2022-06-14 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_body',
            field=models.TextField(),
        ),
    ]