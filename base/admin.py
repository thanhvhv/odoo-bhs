from django.contrib import admin
from .models import Odoo, Module, Demo, Port

# Register your models here.
admin.site.register(Odoo)
admin.site.register(Module)
admin.site.register(Demo)
admin.site.register(Port)