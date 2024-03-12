# Generated by Django 4.2.7 on 2024-02-20 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_doctors_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdata',
            name='checked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='doctors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.doctors'),
        ),
    ]
