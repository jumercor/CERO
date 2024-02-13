from fastapi import APIRouter, HTTPException
from services.appointment_service import (
    get_appointment_by_id,
    modify_fecha_appointment,
    confirmar_appointment,
    cancel_appointment
)

router = APIRouter()

@router.get("/{appointment_id}")
def read_appointment(appointment_id: int):
    appointment = get_appointment_by_id(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

@router.put("/{appointment_id}")
def update_appointment(appointment_id: int):
    appointment = modify_fecha_appointment(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

@router.put("/{appointment_id}/confirm")
def confirm_appointment_route(appointment_id: int):
    appointment = confirmar_appointment(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment


@router.put("/{appointment_id}/cancel")
def confirm_appointment_route(appointment_id: int):
    appointment = cancel_appointment(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

