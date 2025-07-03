from fastapi import FastAPI

app = FastAPI()

import psycopg2

try:
    conn = psycopg2.connect(
        host="mininazem.cj8iguu6cni6.us-east-1.rds.amazonaws.com",
        dbname="nombre_bd",
        user="usuario",
        password="contraseña",
        port=5432
    )
    print("¡Conexión exitosa!")
    conn.close()
except Exception as e:
    print(f"Error: {e}")

@app.get("/")
async def root():
    return {"message": "Hello World"}