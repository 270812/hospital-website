# Generated by Django 5.0.2 on 2024-03-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('home', '0007_alter_user_is_superuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='email ddress')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('is_staff', models.BooleanField(blank=True, default=False, null=True)),
                ('is_admin', models.BooleanField(blank=True, default=False, null=True)),
                ('is_superuser', models.BooleanField(blank=True, default=True, null=True)),
                ('is_doctor', models.BooleanField(blank=True, default=False, null=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='admin_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='admin_user_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
