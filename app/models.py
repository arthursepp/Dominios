# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has on_delete set to the desired behavior
#   * Remove managed = False lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    sobrenome = models.CharField(db_column='Sobrenome', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cnpj_cpf = models.CharField(db_column='CNPJ_CPF', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='Ativo', blank=True, null=True)  # Field name made lowercase.
    data_entrada = models.DateField(db_column='DataEntrada', blank=True, null=True)  # Field name made lowercase.
    data_saida = models.DateField(db_column='DataSaida', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'Cliente'
        
    def __str__(self):
        return f'{self.id} - {self.nome} {self.sobrenome} - Ativo? {self.ativo}'


class Dominio(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='Endereco', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    donoid = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='DonoId')  # Field name made lowercase.
    ativo = models.CharField(db_column='Ativo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    expira_em = models.DateField(db_column='ExpiraEm')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'Dominio'
    
    def __str__(self):
        return f'{self.id} - {self.endereco} - {self.ativo}'