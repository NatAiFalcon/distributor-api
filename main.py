

from typing import Union
from fastapi import FastAPI, HTTPException, APIRouter
import logging
import os
# FastAPI 애플리케이션 생성
app = FastAPI()
router = APIRouter()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/listdir")
def read_dir():
    return os.listdir("../shared/")

@app.get("/uwb/{tag_id}")
def read_item(tag_id: int):
    try:
        temp_filename = "../shared/temp" + str(tag_id)
        with open(temp_filename + ".txt", 'r') as f:
            line = f.readline()
        return line
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=404, detail="Not Vaild tag ID")


app.include_router(router, prefix="/api")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
# uwb의 좌표를 보내는 api server
