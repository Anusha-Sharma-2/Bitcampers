# Generated by Django 4.2.4 on 2023-08-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt_file', models.FileField(upload_to='documents/')),
                ('db_file', models.FileField(upload_to='documents/')),
            ],
        ),
    ]