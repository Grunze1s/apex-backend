# Generated by Django 3.2.13 on 2022-11-02 11:50

from django.db import migrations, models

import report.models


class Migration(migrations.Migration):

    dependencies = [
        ("report", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="generatedreport",
            name="report_file",
            field=models.FileField(
                default="", upload_to=report.models.GeneratedReport.report_upload
            ),
            preserve_default=False,
        ),
    ]
