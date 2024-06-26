# Generated by Django 3.1 on 2020-09-09 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(max_length=256)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('pregnancies', models.IntegerField()),
                ('glucose', models.IntegerField()),
                ('bloodPressure', models.IntegerField()),
                ('skinThickness', models.IntegerField()),
                ('insulin', models.IntegerField()),
                ('bmi', models.FloatField()),
                ('diabetesPedigreeFunction', models.FloatField()),
                ('age', models.IntegerField()),
                ('Result', models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative')], max_length=10)),
                ('users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
