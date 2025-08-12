from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin

class ClienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(models.Cliente, ClienteAdmin)

class DominioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(models.Dominio, DominioAdmin)
