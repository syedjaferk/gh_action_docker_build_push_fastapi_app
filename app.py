from fastapi import FastAPI
from random_id_generator.id_generator import IdGenerator

app = FastAPI()


@app.get("/")
async def index():
   return {"message": "Hello World", "id": IdGenerator().get_random_id()}
