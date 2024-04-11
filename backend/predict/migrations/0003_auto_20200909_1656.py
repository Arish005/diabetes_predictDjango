# Generated by Django 3.1 on 2020-09-09 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('predict', '0002_auto_20200909_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicaldata',
            name='name',
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='Result',
            field=models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='bloodPressure',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='bmi',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='diabetesPedigreeFunction',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='glucose',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='insulin',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='patientName',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='pregnancies',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='skinThickness',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]