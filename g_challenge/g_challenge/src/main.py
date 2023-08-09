import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
    uvicorn.run(app, host="0.0.0.0", port=8001)
