# Generated by Django 4.1.2 on 2023-12-23 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0062_alter_comment_create_date_alter_post_create_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 23, 16, 14, 5, 196687, tzinfo=datetime.timezone.utc)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 23, 16, 14, 5, 196264, tzinfo=datetime.timezone.utc)
            ),
        ),
    ]