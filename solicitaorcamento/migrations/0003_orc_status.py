# Generated by Django 4.0.5 on 2022-06-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitaorcamento', '0002_remove_orc_status_remove_orc_usuario_orc_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orc',
            name='status',
            field=models.CharField(choices=[('P', 'Pendente'), ('F', 'Finalizado')], default='P', max_length=10),
        ),
    ]