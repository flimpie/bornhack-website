# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-12 21:33


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("shop", "0028_auto_20160712_2119")]

    operations = [
        migrations.AlterField(
            model_name="customorder",
            name="customer",
            field=models.TextField(help_text="The customer info for this order"),
        )
    ]
