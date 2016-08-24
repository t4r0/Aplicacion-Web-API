# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class TxcArticulo(models.Model):
    idarticulo = models.AutoField(db_column='idArticulo', primary_key=True)  # Field name made lowercase.
    articulo = models.TextField()
    titulo = models.ForeignKey('TxcTitulo', models.DO_NOTHING, db_column='Titulo_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'txc_articulo'


class TxcPreguntaarticulo(models.Model):
    idpreguntaarticulo = models.AutoField(db_column='idPreguntaArticulo', primary_key=True)  # Field name made lowercase.
    pregunta = models.ForeignKey('TxcPregunta', models.DO_NOTHING, db_column='Pregunta_id')  # Field name made lowercase.
    articulo = models.ForeignKey(TxcArticulo, models.DO_NOTHING, db_column='Articulo_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'txc_preguntaarticulo'


class TxcTitulo(models.Model):
    idtitulo = models.IntegerField(db_column='idTitulo', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txc_titulo'


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
