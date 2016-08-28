# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class TxcActividad(models.Model):
    idactividad = models.AutoField(db_column='idActividad', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txc_actividad'


class TxcArticulo(models.Model):
    idarticulo = models.AutoField(db_column='idArticulo', primary_key=True)  # Field name made lowercase.
    numero = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField()
    titulo_id = models.IntegerField(db_column='Titulo_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'txc_articulo'


class TxcPregunta(models.Model):
    idpregunta = models.AutoField(db_column='idPregunta', primary_key=True)  # Field name made lowercase.
    pregunta = models.TextField()
    respuesta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txc_pregunta'


class TxcPreguntaarticulo(models.Model):
    idpreguntaarticulo = models.AutoField(db_column='idPreguntaArticulo', primary_key=True)  # Field name made lowercase.
    pregunta_id = models.IntegerField(db_column='Pregunta_id')  # Field name made lowercase.
    articulo_id = models.IntegerField(db_column='Articulo_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'txc_preguntaarticulo'


class TxcTitulo(models.Model):
    idtitulo = models.IntegerField(db_column='idTitulo', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txc_titulo'


class TxdBus(models.Model):
    idbus = models.AutoField(db_column='idBus', primary_key=True)  # Field name made lowercase.
    placa = models.CharField(max_length=8)
    color = models.CharField(max_length=20)
    modelo = models.CharField(max_length=45, blank=True, null=True)
    marca = models.CharField(max_length=20)
    numbus = models.IntegerField()
    observaciones = models.TextField(blank=True, null=True)
    foto = models.CharField(max_length=100, blank=True, null=True)
    duenio_id = models.IntegerField(db_column='Duenio_id')  # Field name made lowercase.
    ruta_id = models.IntegerField(db_column='Ruta_id')  # Field name made lowercase.
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txd_bus'


class TxdChofer(models.Model):
    idchofer = models.AutoField(db_column='idChofer', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    dpi = models.IntegerField()
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    foto = models.CharField(max_length=100, blank=True, null=True)
    licencia = models.CharField(max_length=1)
    tipolicencia = models.CharField(db_column='tipoLicencia', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nolicencia = models.IntegerField(db_column='noLicencia', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(blank=True, null=True)
    duenio_id = models.IntegerField(db_column='Duenio_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'txd_chofer'


class TxdDenuncia(models.Model):
    iddenuncia = models.BigIntegerField(db_column='idDenuncia', primary_key=True)  # Field name made lowercase.
    idhash = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    fechahora = models.DateTimeField(blank=True, null=True)
    tipodenuncia_id = models.IntegerField(db_column='Tipodenuncia_id')  # Field name made lowercase.
    placa = models.CharField(max_length=7, blank=True, null=True)
    chofer_id = models.IntegerField(db_column='Chofer_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'txd_denuncia'


class TxdDia(models.Model):
    iddia = models.AutoField(db_column='idDia', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'txd_dia'


class TxdDiahorario(models.Model):
    iddiahorario = models.AutoField(db_column='idDiaHorario', primary_key=True)  # Field name made lowercase.
    horario_id = models.IntegerField(db_column='Horario_id')  # Field name made lowercase.
    dia_id = models.IntegerField(db_column='Dia_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'txd_diahorario'


class TxdDiahorariodetalle(models.Model):
    iddiahorariodetalle = models.AutoField(db_column='idDiaHorarioDetalle', primary_key=True)  # Field name made lowercase.
    bus_id = models.IntegerField(db_column='Bus_id')  # Field name made lowercase.
    chofer_id = models.IntegerField(db_column='Chofer_id')  # Field name made lowercase.
    diahorario_id = models.IntegerField(db_column='DiaHorario_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'txd_diahorariodetalle'


class TxdDuenio(models.Model):
    idduenio = models.AutoField(db_column='idDuenio', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    dpi = models.IntegerField()
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    foto = models.CharField(max_length=100)
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txd_duenio'


class TxdHorario(models.Model):
    idhorario = models.AutoField(db_column='idHorario', primary_key=True)  # Field name made lowercase.
    horainicio = models.TimeField()
    horafin = models.TimeField()
    duenio_id = models.IntegerField(db_column='Duenio_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'txd_horario'


class TxdRecurso(models.Model):
    idrecurso = models.AutoField(db_column='idRecurso', primary_key=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=100, blank=True, null=True)
    denuncia_id = models.IntegerField(db_column='Denuncia_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'txd_recurso'


class TxdRuta(models.Model):
    idruta = models.IntegerField(db_column='idRuta', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    recorrido = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txd_ruta'


class TxdTipodenuncia(models.Model):
    idtipodenuncia = models.IntegerField(db_column='idTipodenuncia', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txd_tipodenuncia'
