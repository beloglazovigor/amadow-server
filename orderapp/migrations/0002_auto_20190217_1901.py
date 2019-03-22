# Generated by Django 2.1.7 on 2019-02-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('FM', 'Checkout'), ('STP', 'Sent to proceed'), ('PRD', 'Proceeded'), ('PD', 'Paid'), ('RDY', 'Ready to issue'), ('CNC', 'Cancelled')], default='FM', max_length=3, verbose_name='Status'),
        ),
    ]