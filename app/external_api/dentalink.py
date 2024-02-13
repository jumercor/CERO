from fastapi import HTTPException
import requests

def obtener_cita(id_cita: int):
    url = "https://api.dentalink.healthatom.com/api/v1/citas/"+str(id_cita)
    headers = {
        "Authorization": "Token ORSHIjmPFwwMq4CHqcBvmWQFXK9folhddG5zLS1Z.PmxwLG6pIGVdZsg2Rbpk0kEW9femNcHgx57YMBAI"
    }


    try:
        response = requests.get(url, headers=headers)

        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            return response.json()
        else:
            # Lanza una excepción si la solicitud no fue exitosa
            raise HTTPException(status_code=response.status_code, detail="Error al obtener la cita")
    except requests.RequestException as e:
        # Captura otras excepciones relacionadas con la solicitud
        raise HTTPException(status_code=500, detail=f"Error de conexión: {str(e)}")


def modificar_status_cita(id_cita: int, status: str, estado_anulacion: bool, estado_confirmacion: bool):
    url = "https://api.dentalink.healthatom.com/api/v1/citas/"+str(id_cita)
    headers = {
        "Authorization": "Token ORSHIjmPFwwMq4CHqcBvmWQFXK9folhddG5zLS1Z.PmxwLG6pIGVdZsg2Rbpk0kEW9femNcHgx57YMBAI"
    }

    # Datos que se enviarán en el cuerpo de la solicitud para modificar el estado de la cita
    data = {"estado_cita": status,
            "estado_anulacion": estado_anulacion,
            "estado_confirmacion": estado_confirmacion}

    try:
        response = requests.put(url, json=data, headers=headers)

        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            return {"mensaje": "Estado de la cita modificado exitosamente"}
        else:
            # Lanza una excepción si la solicitud no fue exitosa
            raise HTTPException(status_code=response.status_code, detail="Error al modificar el estado de la cita")
    except requests.RequestException as e:
        # Captura otras excepciones relacionadas con la solicitud
        raise HTTPException(status_code=500, detail=f"Error de conexión: {str(e)}")
    
def modificar_fecha_cita(id_cita: int, status: str, fecha: str, hora_inicio: str, estado_confirmacion: bool, estado_anulacion: bool):
    url = "https://api.dentalink.healthatom.com/api/v1/citas/"+str(id_cita)
    headers = {
        "Authorization": "Token ORSHIjmPFwwMq4CHqcBvmWQFXK9folhddG5zLS1Z.PmxwLG6pIGVdZsg2Rbpk0kEW9femNcHgx57YMBAI"
    }

    # Datos que se enviarán en el cuerpo de la solicitud para modificar la fecha de la cita
    data = {"estado_cita": status,
            "fecha": fecha,
            "hora_inicio": hora_inicio,
            "estado_confirmacion": estado_confirmacion,
            "estado_anulacion": estado_anulacion}

    try:
        response = requests.put(url, json=data, headers=headers)

        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            return {"mensaje": "Estado de la cita modificado exitosamente"}
        else:
            # Lanza una excepción si la solicitud no fue exitosa
            raise HTTPException(status_code=response.status_code, detail="Error al modificar el estado de la cita")
    except requests.RequestException as e:
        # Captura otras excepciones relacionadas con la solicitud
        raise HTTPException(status_code=500, detail=f"Error de conexión: {str(e)}")



