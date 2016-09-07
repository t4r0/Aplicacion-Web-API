from django.contrib.auth.models import User, Group
from app import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class TxcActividadS(serializers.ModelSerializer):
    class Meta:
        model = models.TxcActividad

class TxcArticuloS(serializers.ModelSerializer):
    class Meta:
        model = models.TxcArticulo

class TxcCapituloS(serializers.ModelSerializer):
    class Meta:
        model = models.TxcCapitulo

class TxcPreguntaarticuloS(serializers.ModelSerializer):
    class Meta:
        model = models.TxcPreguntaarticulo

class TxcTituloS(serializers.ModelSerializer):
    class Meta:
        model = models.TxcTitulo

class TxdBus(serializers.ModelSerializer):
    class Meta:
        model = models.TxdBus

class TxdDenunciaS(serializers.ModelSerializer):
    class Meta:
        model = models.TxdDenuncia

class TxdDiaS(serializers.ModelSerializer):
    class Meta:
        model = models.TxdDia

class TxdDiahorarioS(serializers.ModelSerializer):
    class Meta:
        model = models.TxdDiahorario

class TxdDiahorariodetalleS(serializers.ModelSerializer):
    class Meta:
        model = models.TxdDiahorariodetalle

class TxdDuenioS(serializers.ModelSerializer):
    class Meta:
        model = models.TxdDuenio

class TxdHorarioS(serializers.ModelSerializer):
    class Meta:
        model = models.TxdHorario

class TxdRecursoS(serializers.ModelSerializer):
    class Meta:
        model = models.TxdRecurso

class TxdRutaS(serializers.ModelSerializer):
    class Meta:
        model = models.TxdRuta

class TxdTipodenunciaS(serializers.ModelSerializer):
    class Meta:
        model = models.TxdTipodenuncia
