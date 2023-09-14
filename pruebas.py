import datetime
import time

timestamp = 1694734861.0 # Suponiendo que tienes una marca de tiempo en `timestamp`
fecha_y_hora = datetime.datetime.utcfromtimestamp(timestamp)

# Formatear la fecha y hora según tus preferencias
formato = "%Y-%m-%d %H:%M:%S"  # Puedes ajustar el formato como desees
fecha_formateada = fecha_y_hora.strftime(formato)

print(f"Marca de tiempo UNIX: {timestamp}")
print(f"Fecha y hora formateada: {fecha_formateada}")
