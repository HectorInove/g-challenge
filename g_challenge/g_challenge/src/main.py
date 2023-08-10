import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from g_challenge.src.settings import (
    ENVIRONMENT,
    HOST,
    PORT)
# from app.api.file import fileRouter
# from app.api.chat import chatRouter

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.include_router(fileRouter)
# app.include_router(chatRouter)


@app.get("/")
async def root():
    return {"message": "API running."}


if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host=HOST,
        port=PORT,
        reload=True if ENVIRONMENT =='develop' else False
        )
