# Generated by Django 3.1.6 on 2021-02-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contactform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psychologist',
            name='degree',
            field=models.CharField(choices=[('BS PSYCHOLOGY', 'BS PSYCHOLOGY'), ('MS PSYCHOLOGY', 'MS PSYCHOLOGY'), ('PHD PSYCHOLOGY', 'PHD PSYCHOLOGY')], default='BS PSYCHOLOGY', max_length=100),
        ),
        migrations.AlterField(
            model_name='psychologist',
            name='session_fee',
            field=models.CharField(choices=[('500', '500'), ('1000', '1000'), ('2000', '2000'), ('3000', '3000'), ('4000', '4000'), ('4000', '4000'), ('6000', '6000'), ('7000', '7000'), ('8000', '8000'), ('9000', '9000'), ('10000', '10000')], default='500', max_length=10),
        ),
        migrations.AlterField(
            model_name='psychologist',
            name='specialization',
            field=models.CharField(choices=[('CLINICAL PSYCHOLOGY', 'CLINICAL PSYCHOLOGY'), ('COUNSELING PSYCHOLOGY', 'COUNSELING PSYCHOLOGY'), ('DEVELOPMENTAL PSYCHOLOGY', 'DEVELOPMENTAL PSYCHOLOGY'), ('EDUCATIONAL PSYCHOLOGY', 'EDUCATIONAL PSYCHOLOGY'), ('EVIRONMENTAL PSYCHOLOGY', 'EVIRONMENTAL PSYCHOLOGY'), ('EXPERIMENTAL PSYCHOLOGY', 'EXPERIMENTAL PSYCHOLOGY'), ('FORENSIC PSYCHOLOGY', 'FORENSIC PSYCHOLOGY'), ('HUMAN FACTORS PSYCHOLOGY', 'HUMAN FACTORS PSYCHOLOGY'), ('SCHOOL PSYCHOLOGY', 'SCHOOL PSYCHOLOGY'), ('SOCIAL PSYCHOLOGY', 'SOCIAL PSYCHOLOGY'), ('SPORT PSYCHOLOGY', 'SPORT PSYCHOLOGY')], default='SPORT PSYCHOLOGY', max_length=100),
        ),
    ]