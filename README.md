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