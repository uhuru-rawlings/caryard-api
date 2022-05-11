# Generated by Django 4.0.4 on 2022-05-11 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='cars',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='api.cars'),
        ),
        migrations.AddField(
            model_name='replies',
            name='messageid',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='api.messages'),
        ),
        migrations.AlterField(
            model_name='replies',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.registration'),
        ),
    ]