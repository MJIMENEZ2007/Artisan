# Generated by Django 5.0.4 on 2024-08-21 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DniProcesos',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('idoperario', models.CharField(blank=True, db_column='IdOperario', max_length=60, null=True)),
                ('idseccion', models.CharField(blank=True, db_column='IdSeccion', max_length=30, null=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Procesos',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('idordenproduccion', models.CharField(db_column='IdOrdenProduccion', max_length=100)),
                ('idoperario', models.CharField(db_column='IdOperario', max_length=100)),
                ('idseccion', models.CharField(db_column='IdSeccion', max_length=100)),
                ('fechahora', models.CharField(blank=True, db_column='FechaHora', max_length=50, null=True)),
                ('tipo', models.CharField(blank=True, db_column='Tipo', max_length=15, null=True)),
                ('modelo', models.CharField(blank=True, db_column='Modelo', max_length=50, null=True)),
                ('categoría', models.CharField(blank=True, db_column='Categoria', max_length=50, null=True)),
                ('tarifa', models.DecimalField(blank=True, db_column='Tarifa', decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seccionesexcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion', models.CharField(blank=True, max_length=255, null=True)),
                ('libro', models.CharField(blank=True, max_length=255, null=True)),
                ('recepcion_fecha', models.CharField(blank=True, max_length=255, null=True)),
                ('asignacion_fecha', models.CharField(blank=True, max_length=255, null=True)),
                ('asignacion_persona', models.CharField(blank=True, max_length=255, null=True)),
                ('final_fecha', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
