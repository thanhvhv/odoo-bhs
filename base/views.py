from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from .models import Odoo, Module, Demo, Port
from django.http import JsonResponse
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import time

def index(request):
    odoos = Odoo.objects.all()
    modules = Module.objects.all()
    demos = Demo.objects.all().order_by('-datetime')
    ports = Port.objects.all()
    demo = Demo()
    command = './odoo/odoo_controller/deploy.sh'
    if request.method == 'POST':
        # create new demo
        if request.POST.get('version') is not None:
            demo.name = request.POST.get('app')
            demo.port = request.POST.get('port')
            demo.version = Odoo.objects.get(version=int(request.POST.get('version')))
            demo.state = "Starting"
            demo.save()

            # run command
            command = command + ' ' + request.POST.get('app')
            command = command + ' ' + request.POST.get('port')
            command = command + ' ' + request.POST.get('version')
            for module in modules:
                if request.POST.get('module-'+str(module.id)) is not None:
                    command = command + ' ' + module.name
                    module.demo.add(demo)
            subprocess.run([command], shell=True)
            cp_backup_command = 'docker cp ./odoo/odoo_controller/sample_db.sql ' + demo.name + '_db_1:/'
            subprocess.run([cp_backup_command], shell=True)
        if request.POST.get('restore') is not None:
            restore_command = 'docker exec -i ' + request.POST.get('restore') + '_db_1 ' + 'psql -U odoo -d mydb -f sample_db.sql'
            subprocess.run([restore_command], shell=True)
            demo = Demo.objects.get(id=request.POST.get('demo-id-restore'))
            demo.restore = True
            demo.save()
   
        if request.POST.get('start-demo') is not None:
            id_start = request.POST.get('start-demo')
            demo_start = Demo.objects.get(id=id_start)
            command_start = './odoo/odoo_controller/start.sh '
            command_start = command_start + demo_start.name
            subprocess.run([command_start], shell=True)
            demo_start.state = "Starting"
            demo_start.save()    

        if request.POST.get('stop-demo') is not None:
            id_stop = request.POST.get('stop-demo')
            demo_stop = Demo.objects.get(id=id_stop)
            command_stop = './odoo/odoo_controller/stop.sh '
            command_stop = command_stop + demo_stop.name
            subprocess.run([command_stop], shell=True)
            demo_stop.state = "Stopped"
            demo_stop.save()

        if request.POST.get('destroy-demo') is not None:
            id_destroy = request.POST.get('destroy-demo')
            demo_destroy = Demo.objects.get(id=id_destroy)
            command_destroy = './odoo/odoo_controller/destroy.sh '
            command_destroy = command_destroy + demo_destroy.name
            subprocess.run([command_destroy], shell=True)
            demo_destroy.state = "Destroyed"
            print(datetime.now())
            print(demo_destroy.datetime)
            demo_destroy.duration = datetime.now() - demo_destroy.datetime.replace(tzinfo=None)
            demo_destroy.save()
    for demo in demos:
        demo.duration = str(demo.duration).split('.')[0]
    demos_available = Demo.objects.exclude(state='Destroyed')
    ports_avaiable = []
    for port in ports:
        temp = 0
        for demo in demos_available:
            if demo.port == port.port:
                temp = 1
                break
        if temp == 0:
            ports_avaiable.append(port.port)
    starting = Demo.objects.filter(state='Starting').first()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if starting is not None:
            target_url = 'http://192.168.3.28:' + str(starting.port)  # Replace with the website you want to check
            print(target_url)
            try:
                response = requests.get(target_url)
                status_code = response.status_code
                if response.ok:
                    starting.state = 'Running'
                    starting.save()
                    return JsonResponse({'status': 'Available', 'port':starting.port}, status=200)
                else:
                    return JsonResponse({'status': f'Other Error: {status_code}', 'port':starting.port}, status=status_code)
            except requests.RequestException as e:
                return JsonResponse({'status': 'Error', 'error': str(e), 'port':starting.port}, status=500)
        else:
            return JsonResponse({'status': 'None'})
    
    context = {'odoos':odoos, 'modules':modules, 'demos':demos, 'demos_available':demos_available, 'ports':ports, 'ports_avaiable':ports_avaiable}
    return render(request, "base/index.html", context)

def check(request):

    context = {}
    return render(request, "base/check.html", context)
