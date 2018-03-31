# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-17 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpressTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_request', models.TextField(max_length=512)),
                ('raw_response', models.TextField(max_length=512)),
                ('response_time', models.FloatField(help_text='Response time in milliseconds')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('method', models.CharField(max_length=32)),
                ('version', models.CharField(max_length=8)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('currency', models.CharField(blank=True, max_length=8, null=True)),
                ('ack', models.CharField(max_length=32)),
                ('correlation_id', models.CharField(blank=True, max_length=32, null=True)),
                ('token', models.CharField(blank=True, max_length=32, null=True)),
                ('error_code', models.CharField(blank=True, max_length=32, null=True)),
                ('error_message', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='PayflowTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_request', models.TextField(max_length=512)),
                ('raw_response', models.TextField(max_length=512)),
                ('response_time', models.FloatField(help_text='Response time in milliseconds')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('comment1', models.CharField(db_index=True, max_length=128, verbose_name='Comment 1')),
                ('trxtype', models.CharField(max_length=12, verbose_name='Transaction type')),
                ('tender', models.CharField(max_length=12, null=True, verbose_name='Bankcard or PayPal')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('pnref', models.CharField(max_length=32, null=True, verbose_name='Payflow transaction ID')),
                ('ppref', models.CharField(max_length=32, null=True, unique=True, verbose_name='Payment transaction ID')),
                ('result', models.CharField(blank=True, max_length=32, null=True)),
                ('respmsg', models.CharField(max_length=512, verbose_name='Response message')),
                ('authcode', models.CharField(blank=True, max_length=32, null=True, verbose_name='Auth code')),
                ('cvv2match', models.CharField(blank=True, max_length=12, null=True, verbose_name='CVV2 check')),
                ('avsaddr', models.CharField(blank=True, max_length=1, null=True, verbose_name='House number check')),
                ('avszip', models.CharField(blank=True, max_length=1, null=True, verbose_name='Zip/Postcode check')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
