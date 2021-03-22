# Generated by Django 3.1.7 on 2021-03-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentID', models.BigIntegerField()),
                ('Student_name', models.CharField(max_length=255)),
                ('Branch', models.CharField(max_length=3)),
                ('PhoneNo', models.IntegerField()),
                ('Address', models.CharField(max_length=255)),
                ('Country', models.CharField(max_length=255)),
                ('Tenth', models.CharField(max_length=255)),
                ('Twelvth', models.CharField(max_length=255)),
                ('Present_Cgpa', models.FloatField(max_length=3)),
                ('Total_backlogs', models.IntegerField()),
                ('Active_backlogs', models.IntegerField()),
                ('Placement_status', models.BooleanField(default=False)),
                ('TCS', models.CharField(max_length=10)),
                ('Cognizant', models.CharField(max_length=10)),
                ('Capgemini', models.CharField(max_length=10)),
                ('MindTree', models.CharField(max_length=10)),
                ('Infosys', models.CharField(max_length=10)),
                ('Wipro', models.CharField(max_length=10)),
                ('Deloitte', models.CharField(max_length=10)),
                ('HCL', models.CharField(max_length=10)),
                ('Accenture', models.CharField(max_length=10)),
                ('IBM', models.CharField(max_length=10)),
            ],
        ),
    ]
