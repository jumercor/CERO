# CERO

## Requisitos

- Python (versión 3.12.2^)

## Instalación

1. Clona el repositorio
2. Navega al directorio del proyecto
4. Preferiblemente activa tu `venv`
3. Instala las dependencias `pip install -r requirements.txt`

## Uso

Para ejecutar la aplicación, puedes usar Uvicorn. Asegúrate de activar tu entorno virtual antes de ejecutar estos comandos.

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --log-level debug
```

Esto iniciará el servidor FastAPI y estará disponible en http://localhost:8000.

Los endpoints disponibles son:

GET {{base_url}}/api/v1/appointments/{appointment_id} -> Obtener una cita por su id
GET {{base_url}}/api/vi/appintments/ -> Para filtrar citas por fecha, estado y sucursal (ojo, todos se deben incluir) se deben incluir los parametros  fecha_inicio, fecha_fin (con esto filtra por la fecha de la cita)id_estado, id_sucursal. Ejemplo:  {{base_url}}/api/vi/appintments/?fecha_inicio=2016-11-01&fecha_fin=2024-12-01&id_estado=1&id_sucursal=2
PUT {{base_url}}/api/v1/appointments/{appointment_id}/modificar_estado para modificar el estado de una cita. En la url se debe especificar el id del nuevo estado, de esta forma {{base_url}}/api/v1/appointments/1/modificar_estado/?id_estado=# 
