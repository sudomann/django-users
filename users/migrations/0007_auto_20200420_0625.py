# Generated by Django 2.2.9 on 2020-04-20 10:25

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_privacypolicy_securitypolicy_termsofservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='privacy_policy_version',
            field=models.ForeignKey(default=users.models.get_current_privacy, on_delete=django.db.models.deletion.PROTECT, to='users.PrivacyPolicy'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='security_policy_version',
            field=models.ForeignKey(default=users.models.get_current_security, on_delete=django.db.models.deletion.PROTECT, to='users.SecurityPolicy'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='terms_of_service_version',
            field=models.ForeignKey(default=users.models.get_current_terms, on_delete=django.db.models.deletion.PROTECT, to='users.TermsOfService'),
        ),
    ]