# Generated by Django 5.1.3 on 2024-11-27 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_producto_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='estado',
            field=models.CharField(choices=[(1, 'Disponible'), (0, 'Agotado')], default=1, max_length=10),
        ),
    ]