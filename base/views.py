from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from .models import Odoo, Module

def index(request):
    odoos = Odoo.objects.all()
    modules = Module.objects.all()
    command = './odoo_controller/deploy.sh'
    if request.method == 'POST':
        command = command + ' ' + request.POST.get('app')
        command = command + ' ' + request.POST.get('port')
        command = command + ' ' + request.POST.get('version')
        for module in modules:
            if request.POST.get('module-'+str(module.id)) is not None:
                command = command + ' ' + module.name
        subprocess.run([command], shell=True)
        
    print(command)
    
    context = {'odoos':odoos, 'modules':modules}
    return render(request, "base/index.html", context)