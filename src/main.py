import uvicorn
import logging

from fastapi import FastAPI

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


if __name__ == "__main__":
    log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    log_file_name = "server.log"
    logging.basicConfig(filename=log_file_name, level=logging.DEBUG, format=log_format)
    # logging.getLogger("asyncio").setLevel(logging.WARNING)

    config = uvicorn.Config("main:app", port=5000, log_level="debug")
    server = uvicorn.Server(config)
    server.run()

