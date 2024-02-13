from typing import Optional
from models.appointment import Appointment
import external_api.dentalink as dentalink

def get_appointment_by_id(appointment_id: int) -> Optional[Appointment]:
    # Lógica para obtener la cita por ID
    cita = dentalink.obtener_cita(appointment_id)
    return cita

def confirmar_appointment(appointment_id: int) -> Optional[Appointment]:
    # Lógica para modificar el status de la cita por ID
    cita_modificada = dentalink.modificar_status_cita(appointment_id, "Confirmada", 0 , 1)
    return cita_modificada

def cancel_appointment(appointment_id: int) -> Optional[Appointment]:
    # Lógica para cancelar la cita por ID
    cita_cancelada = dentalink.modificar_status_cita(appointment_id, "Cancelada", 1, 0)
    return cita_cancelada

def modify_fecha_appointment(appointment_id: int, fecha, hora_inicio) -> Optional[Appointment]:
    # Lógica para confirmar la fecha de la cita y dejarla confirmada
    cita_fecha_modificada = dentalink.modificar_fecha_cita(appointment_id, "Confirmada", fecha, hora_inicio, 0, 1)
    return cita_fecha_modificada
