from fastapi import FastAPI, Body
from models import Text
import uvicorn


app = FastAPI()

@app.post("/latin-to-kirill", response_model=Text)
async def getLatinToKirill(text: Text):
    """ For Latin to Kirill conversion """
    text.toKirill()
    
    return text


@app.post("/kirill-to-latin", response_model=Text)
async def getLatinToKiril(text: Text):
    """ For Kirill to Latin conversion """
    text.toLatin()
    
    return text


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=1234, reload=True)