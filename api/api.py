from fastapi import FastAPI
import logging

from commonutils.utils import set_logger_config

logger = set_logger_config(logging)
app = FastAPI()


@app.get("/test")
async def list():
    return {
        "success": "response"
    }
