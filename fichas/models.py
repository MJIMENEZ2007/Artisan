from django.db import models


class DniProcesos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idoperario = models.CharField(db_column='IdOperario', max_length=60, blank=True, null=True)  # Field name made lowercase.
    idseccion = models.CharField(db_column='IdSeccion', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100, blank=True, null=True)





class Procesos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idordenproduccion = models.CharField(db_column='IdOrdenProduccion', max_length=100)  # Field name made lowercase.
    idoperario = models.CharField(db_column='IdOperario', max_length=100)  # Field name made lowercase.
    idseccion = models.CharField(db_column='IdSeccion', max_length=100)  # Field name made lowercase.
    fechahora = models.CharField(db_column='FechaHora', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    categoría = models.CharField(db_column='Categoria', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tarifa = models.DecimalField(db_column='Tarifa', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.




class Seccionesexcel(models.Model):
    seccion = models.CharField(max_length=255, blank=True, null=True)
    libro = models.CharField(max_length=255, blank=True, null=True)
    recepcion_fecha = models.CharField(max_length=255, blank=True, null=True)
    asignacion_fecha = models.CharField(max_length=255, blank=True, null=True)
    asignacion_persona = models.CharField(max_length=255, blank=True, null=True)
    final_fecha = models.CharField(max_length=255, blank=True, null=True)

