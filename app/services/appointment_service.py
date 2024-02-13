from typing import Optional
from models.appointment import Appointment
import external_api.dentalink as dentalink
import json

def get_appointment_by_id(appointment_id: int) -> Optional[Appointment]:
    # Lógica para obtener la cita por ID
    cita = dentalink.obtener_cita(appointment_id)
    return cita

def filter_appointments_by(fecha_inicio: str, fecha_fin: str, id_sucursal: int, id_estado: int) -> Optional[Appointment]:
    fecha_inicio = fecha_inicio
    fecha_fin = fecha_fin
    id_sucursal = id_sucursal
    id_estado = id_estado
    citasFiltradas = []
    cita = dentalink.obtener_citas()
#¿por qué hice este bucle? porque cuando intenté filtrar con los parametros que entregaba la API por algún motivo no funcionaba, lo intenté de muchas formas (incluso directamente en jupiternotebook)
#se que debería ser responsabilidad de la api del cliente tener los filtros (o no, dependiendo de que politicas tenga CERO para estos casos)
#pero bueno, para resolver el ejercicio decidí hacer el filtro yo dentro del código
    for i in cita["data"]:
        if (fecha_inicio <= i["fecha"] <= fecha_fin) and i["id_sucursal"] == id_sucursal and i["id_estado"] == id_estado:
            citasFiltradas.append(i)


    return citasFiltradas

def modificar_estado_appointment(appointment_id: int, id_estado: int) -> Optional[Appointment]:
    # Lógica para modificar el status de la cita por ID
    cita_modificada = dentalink.modificar_status_cita(appointment_id, id_estado)
    return cita_modificada
