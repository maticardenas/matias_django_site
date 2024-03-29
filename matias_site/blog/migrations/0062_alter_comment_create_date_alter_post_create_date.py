# Generated by Django 4.1.2 on 2023-12-21 20:07

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0061_alter_comment_create_date_alter_post_create_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 21, 20, 6, 58, 950551, tzinfo=datetime.timezone.utc)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 21, 20, 6, 58, 949970, tzinfo=datetime.timezone.utc)
            ),
        ),
    ]
