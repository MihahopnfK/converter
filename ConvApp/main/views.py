from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import file_storageForm
from .models import file_storage
import numpy as np

#from ..ConvApp import settings
#from ..ConvApp.settings import BASE_DIR

def index(request):
    data = {
        'title': 'Главная страница',
    }
    if request.method == 'POST':
        form = file_storageForm(request.POST, request.FILES)
        if form.is_valid():
            stl_file = form.save()
            stl_filename = stl_file.file.path
            gcode_filename = os.path.join(os.path.dirname(stl_filename), 'output.gcode')


            with open(stl_filename, 'r') as stl_file, open(gcode_filename, 'w') as gcode_file:
                for line in stl_file:
                    if line.strip().startswith('vertex'):
                        parts = line.split()
                        x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                        gcode_file.write(f'G1 X{x:.3f} Y{y:.3f} Z{z:.3f} F100\n')

            add_gcode_header(gcode_filename)
            with open(gcode_filename, 'r') as gcode_file:
                gcode_output = gcode_file.read()

            data['gcode_output'] = gcode_output
            if 'gcode_output' in data:
                data['show_gcode'] = True

            data['gcode_output'] = gcode_output
            if 'gcode_output' in data:
                data['show_gcode'] = True
                #data['gcode_download'] = True  # Add this line
                response = HttpResponse(gcode_output, content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename="output.gcode"'
                #return response
        else:
            data['error'] = 'Only STL files are allowed.'

            #return redirect('home')  # Перенаправляем на ту же страницу
    else:
        form = file_storageForm()
    data['form'] = form

    return render(request, 'main/index.html', data)  #{'title': 'Главная страница'} )


def about(request):
    return render(request, 'main/about.html')

def add_gcode_header(gcode_filename):
    header_commands = [
        '; G-code header generated by Python script',
        'G21 ; Set units to millimeters',
        'G90 ; Absolute mode',
        'M82 ; Set extruder to absolute mode',
        'M104 S210 ; Set hotend temperature to 210°C',
        'M109 S210 ; Wait for hotend to reach 210°C',
        'M140 S60 ; Set bed temperature to 60°C',
        'M106 S255 ; Set fan speed to 100%',
        'G28 ; Home all axes',
        'G1 Z0.2 F300 ; Move to safe height',
        'G1 F300 ; Set movement speed to 300 mm/min',
        'M82 ; Set extruder to absolute mode',
        'M83 ; Set extruder to relative mode',
    ]
    with open(gcode_filename, 'r+') as gcode_file:
        content = gcode_file.read()
        gcode_file.seek(0)
        gcode_file.write('\n'.join(header_commands) + '\n' + content)

#def download_gcode(request):
 #   gcode_filename = request.session.get('gcode_filename')
  #  if gcode_filename:
   #     with open(gcode_filename, 'rb') as f:
    #        response = HttpResponse(f.read(), content_type='application/octet-stream')
     #       response['Content-Disposition'] = 'attachment; filename="output.gcode"'
      #      return response
    #return HttpResponseNotFound('G-Code file not found')