# Generated by Django 2.1 on 2019-05-31 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20190531_0527'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article_Comment',
        ),
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
    ]
