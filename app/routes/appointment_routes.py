from fastapi import APIRouter, HTTPException
from services.appointment_service import (
    get_appointment_by_id,
    modificar_estado_appointment,
    filter_appointments_by
)

router = APIRouter()

#Ruta para obtener citas por id
@router.get("/{appointment_id}")
def read_appointment(appointment_id: int):
    appointment = get_appointment_by_id(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

#ruta para filtrar las citas por fechas, estado y sucursal
#los parametros se deben enviar en la url del request, de la siquiente forma: ?fecha_inicio=2016-11-01&fecha_fin=2024-12-01&id_estado=1&id_sucursal=2
@router.get("/")
def read_appointment(fecha_inicio: str, fecha_fin: str, id_estado: int, id_sucursal: int):
    appointment = filter_appointments_by(fecha_inicio, fecha_fin, id_estado, id_sucursal)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

#Por ahora esta ruta la cree para confirmar o cancelar la cita, ya que hay varios estados para confirmar y cancelar y para terminos del ejercicio lo hice lo más sencillo posible
@router.put("/{appointment_id}/modificar_estado")
def confirm_appointment_route(appointment_id: int, id_estado: int):
    appointment = modificar_estado_appointment(appointment_id, id_estado)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment



