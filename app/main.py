from fastapi import FastAPI
from routes.appointment_routes import router as appointment_router


app = FastAPI()

# Incluimos las rutas relacionadas con las citas
app.include_router(appointment_router, prefix="/api/v1/appointments")

if __name__ == "_main_":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")