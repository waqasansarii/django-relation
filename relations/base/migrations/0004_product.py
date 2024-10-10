# Generated by Django 5.1.2 on 2024-10-10 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_delete_student_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='base.category')),
            ],
        ),
    ]
