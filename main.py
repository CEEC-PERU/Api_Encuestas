from fastapi import FastAPI
from app.api.v1.routers import roles  # Asegúrate de que esta importación sea correcta según tu estructura

app = FastAPI()

# Incluye el router de roles
app.include_router(roles.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}