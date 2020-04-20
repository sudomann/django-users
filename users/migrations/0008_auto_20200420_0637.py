# Generated by Django 2.2.9 on 2020-04-20 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200420_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='privacy_policy_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.PrivacyPolicy'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='security_policy_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.SecurityPolicy'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='terms_of_service_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.TermsOfService'),
        ),
    ]
