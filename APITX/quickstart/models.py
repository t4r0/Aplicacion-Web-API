# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Actividad(models.Model):
    idactividad = models.AutoField(db_column='idActividad', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'actividad'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bus(models.Model):
    idbus = models.AutoField(db_column='idBus', primary_key=True)  # Field name made lowercase.
    placa = models.CharField(max_length=8)
    color = models.CharField(max_length=20)
    modelo = models.CharField(max_length=45)
    marca = models.CharField(max_length=20)
    numbus = models.IntegerField()
    observaciones = models.TextField(blank=True, null=True)
    foto = models.CharField(max_length=100, blank=True, null=True)
    duenio = models.ForeignKey('Duenio', models.DO_NOTHING, db_column='Duenio_id')  # Field name made lowercase.
    ruta = models.ForeignKey('Ruta', models.DO_NOTHING, db_column='Ruta_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bus'


class Chofer(models.Model):
    idchofer = models.AutoField(db_column='idChofer', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    dpi = models.CharField(max_length=13)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    foto = models.CharField(max_length=100, blank=True, null=True)
    licencia = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'chofer'


class Denuncia(models.Model):
    iddenuncia = models.AutoField(db_column='idDenuncia', primary_key=True)  # Field name made lowercase.
    denuncia = models.TextField()
    estado = models.IntegerField(blank=True, null=True)
    bus = models.ForeignKey(Bus, models.DO_NOTHING, db_column='Bus_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'denuncia'


class Dia(models.Model):
    iddia = models.AutoField(db_column='idDia', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'dia'


class Diahorario(models.Model):
    iddiahorario = models.AutoField(db_column='idDiaHorario', primary_key=True)  # Field name made lowercase.
    horario = models.ForeignKey('Horarios', models.DO_NOTHING, db_column='Horario_id')  # Field name made lowercase.
    dia = models.ForeignKey(Dia, models.DO_NOTHING, db_column='Dia_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diahorario'


class Diahorariodetalle(models.Model):
    iddiahorariodetalle = models.AutoField(db_column='idDiaHorarioDetalle', primary_key=True)  # Field name made lowercase.
    bus = models.ForeignKey(Bus, models.DO_NOTHING, db_column='Bus_id')  # Field name made lowercase.
    chofer = models.ForeignKey(Chofer, models.DO_NOTHING, db_column='Chofer_id')  # Field name made lowercase.
    diahorario = models.ForeignKey(Diahorario, models.DO_NOTHING, db_column='DiaHorario_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diahorariodetalle'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Duenio(models.Model):
    idduenio = models.AutoField(db_column='idDuenio', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    dpi = models.IntegerField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    foto = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'duenio'


class Dueniochofer(models.Model):
    iddueniochofer = models.IntegerField(db_column='idDuenioChofer', primary_key=True)  # Field name made lowercase.
    duenio = models.ForeignKey(Duenio, models.DO_NOTHING, db_column='Duenio_id')  # Field name made lowercase.
    chofer = models.ForeignKey(Chofer, models.DO_NOTHING, db_column='Chofer_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dueniochofer'


class Horarios(models.Model):
    idhorario = models.AutoField(db_column='idHorario', primary_key=True)  # Field name made lowercase.
    horainicio = models.TimeField()
    horafin = models.TimeField()
    duenio = models.ForeignKey(Duenio, models.DO_NOTHING, db_column='Duenio_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'horarios'


class Ley(models.Model):
    idley = models.AutoField(db_column='idLey', primary_key=True)  # Field name made lowercase.
    ley = models.TextField()

    class Meta:
        managed = False
        db_table = 'ley'


class Pregunta(models.Model):
    idpregunta = models.AutoField(db_column='idPregunta', primary_key=True)  # Field name made lowercase.
    pregunta = models.TextField()
    respuesta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pregunta'


class Preguntaley(models.Model):
    idpreguntaley = models.AutoField(db_column='idPreguntaLey', primary_key=True)  # Field name made lowercase.
    pregunta = models.ForeignKey(Pregunta, models.DO_NOTHING, db_column='Pregunta_id')  # Field name made lowercase.
    ley = models.ForeignKey(Ley, models.DO_NOTHING, db_column='Ley_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preguntaley'


class Recurso(models.Model):
    idrecurso = models.AutoField(db_column='idRecurso', primary_key=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=100, blank=True, null=True)
    denuncia = models.ForeignKey(Denuncia, models.DO_NOTHING, db_column='Denuncia_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recurso'


class Ruta(models.Model):
    idruta = models.IntegerField(db_column='idRuta', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ruta'
