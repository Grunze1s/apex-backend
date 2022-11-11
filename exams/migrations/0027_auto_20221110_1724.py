# Generated by Django 3.2.13 on 2022-11-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exams", "0026_exam_exam_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="exam",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="exam",
            name="publish_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
