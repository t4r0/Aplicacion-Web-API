# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TxcActividad',
            fields=[
                ('idactividad', models.AutoField(db_column='idActividad', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('lugar', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'txc_actividad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxcArticulo',
            fields=[
                ('idarticulo', models.AutoField(db_column='idArticulo', primary_key=True, serialize=False)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('descripcion', models.TextField()),
                ('titulo_id', models.IntegerField(db_column='Titulo_id')),
            ],
            options={
                'db_table': 'txc_articulo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxcPregunta',
            fields=[
                ('idpregunta', models.AutoField(db_column='idPregunta', primary_key=True, serialize=False)),
                ('pregunta', models.TextField()),
                ('respuesta', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'txc_pregunta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxcPreguntaarticulo',
            fields=[
                ('idpreguntaarticulo', models.AutoField(db_column='idPreguntaArticulo', primary_key=True, serialize=False)),
                ('pregunta_id', models.IntegerField(db_column='Pregunta_id')),
                ('articulo_id', models.IntegerField(db_column='Articulo_id')),
            ],
            options={
                'db_table': 'txc_preguntaarticulo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxcTitulo',
            fields=[
                ('idtitulo', models.IntegerField(db_column='idTitulo', primary_key=True, serialize=False)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'txc_titulo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxdBus',
            fields=[
                ('idbus', models.AutoField(db_column='idBus', primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=8)),
                ('color', models.CharField(max_length=20)),
                ('modelo', models.CharField(blank=True, max_length=45, null=True)),
                ('marca', models.CharField(max_length=20)),
                ('numbus', models.IntegerField()),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('foto', models.CharField(blank=True, max_length=100, null=True)),
                ('duenio_id', models.IntegerField(db_column='Duenio_id')),
                ('ruta_id', models.IntegerField(db_column='Ruta_id')),
                ('estado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'txd_bus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxdChofer',
            fields=[
                ('idchofer', models.AutoField(db_column='idChofer', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=45)),
                ('direccion', models.CharField(blank=True, max_length=45, null=True)),
                ('dpi', models.IntegerField()),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('correo', models.CharField(blank=True, max_length=45, null=True)),
                ('foto', models.CharField(blank=True, max_length=100, null=True)),
                ('licencia', models.CharField(max_length=1)),
                ('tipolicencia', models.CharField(blank=True, db_column='tipoLicencia', max_length=2, null=True)),
                ('nolicencia', models.IntegerField(blank=True, db_column='noLicencia', null=True)),
                ('estado', models.IntegerField(blank=True, null=True)),
                ('duenio_id', models.IntegerField(db_column='Duenio_id')),
            ],
            options={
                'db_table': 'txd_chofer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxdDenuncia',
            fields=[
                ('iddenuncia', models.BigIntegerField(db_column='idDenuncia', primary_key=True, serialize=False)),
                ('idhash', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado', models.IntegerField(blank=True, null=True)),
                ('fechahora', models.DateTimeField(blank=True, null=True)),
                ('tipodenuncia_id', models.IntegerField(db_column='Tipodenuncia_id')),
                ('placa', models.CharField(blank=True, max_length=7, null=True)),
                ('chofer_id', models.IntegerField(blank=True, db_column='Chofer_id', null=True)),
            ],
            options={
                'db_table': 'txd_denuncia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxdDia',
            fields=[
                ('iddia', models.AutoField(db_column='idDia', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'txd_dia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxdDiahorario',
            fields=[
                ('iddiahorario', models.AutoField(db_column='idDiaHorario', primary_key=True, serialize=False)),
                ('horario_id', models.IntegerField(db_column='Horario_id')),
                ('dia_id', models.IntegerField(db_column='Dia_id')),
            ],
            options={
                'db_table': 'txd_diahorario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxdDiahorariodetalle',
            fields=[
                ('iddiahorariodetalle', models.AutoField(db_column='idDiaHorarioDetalle', primary_key=True, serialize=False)),
                ('bus_id', models.IntegerField(db_column='Bus_id')),
                ('chofer_id', models.IntegerField(db_column='Chofer_id')),
                ('diahorario_id', models.IntegerField(db_column='DiaHorario_id')),
            ],
            options={
                'db_table': 'txd_diahorariodetalle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxdDuenio',
            fields=[
                ('idduenio', models.AutoField(db_column='idDuenio', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
                ('dpi', models.IntegerField()),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('correo', models.CharField(blank=True, max_length=45, null=True)),
                ('foto', models.CharField(max_length=100)),
                ('estado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'txd_duenio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxdHorario',
            fields=[
                ('idhorario', models.AutoField(db_column='idHorario', primary_key=True, serialize=False)),
                ('horainicio', models.TimeField()),
                ('horafin', models.TimeField()),
                ('duenio_id', models.IntegerField(db_column='Duenio_id')),
            ],
            options={
                'db_table': 'txd_horario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxdRecurso',
            fields=[
                ('idrecurso', models.AutoField(db_column='idRecurso', primary_key=True, serialize=False)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('denuncia_id', models.IntegerField(db_column='Denuncia_id')),
            ],
            options={
                'db_table': 'txd_recurso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxdRuta',
            fields=[
                ('idruta', models.IntegerField(db_column='idRuta', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('recorrido', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'txd_ruta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TxdTipodenuncia',
            fields=[
                ('idtipodenuncia', models.IntegerField(db_column='idTipodenuncia', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'txd_tipodenuncia',
                'managed': False,
            },
        ),
    ]