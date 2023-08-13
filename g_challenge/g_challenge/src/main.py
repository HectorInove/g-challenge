import uvicorn
import argparse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from g_challenge.src.core.db.create_schemas import create_all_schemas
from g_challenge.src.v1.application_apis import router as application_apis
from g_challenge.src.settings import (
    ENVIRONMENT,
    HOST,
    PORT)

parser = argparse.ArgumentParser()
parser.add_argument('--createschemas', type=bool, required=False)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(application_apis)



if __name__ == "__main__":
    args = parser.parse_args()
    print(args.createschemas)
    if args.createschemas:
        create_all_schemas()
    
    uvicorn.run(
        'main:app',
        host=HOST,
        port=PORT,
        reload=True if ENVIRONMENT =='develop' else False
        )
