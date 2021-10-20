import logging
from fastapi import FastAPI, Response

logger = logging.getLogger("main")

app = FastAPI(debug=True)

INMEMORY_REPLICAS_LIST = []


@app.get("/replicas")
def get_message():
    return INMEMORY_REPLICAS_LIST
