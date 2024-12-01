from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.config import config
from validation.validation import Person

import functions.database as MongoAPI

import json


app = FastAPI()


@app.post("/drivers", response_model=Person)
async def create_person(request: Person):
    state = MongoAPI.insert_item(request.json(), config["collections"]['drivers'])
    if state['status'] != "fail":
        return JSONResponse(content=jsonable_encoder(state), status_code=status.HTTP_201_CREATED)
    else:
        return JSONResponse(content=jsonable_encoder(state), status_code=status.HTTP_400_BAD_REQUEST)

@app.get("/drivers")
async def get_person():
    data = MongoAPI.select_all(config["collections"]['drivers'])
    return JSONResponse(content=jsonable_encoder(json.dumps(data, indent=2)), status_code=status.HTTP_200_OK)

@app.get("/driver/<id>")
async def get_person(id):
    data = MongoAPI.select_one({"id": int(id)}, config["collections"]['drivers'])
    return JSONResponse(content=jsonable_encoder(json.dumps(data, indent=2)), status_code=status.HTTP_200_OK)