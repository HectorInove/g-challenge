from fastapi import FastAPI, File, UploadFile

from fastapi import APIRouter
from g_challenge.src.core.db.jobs import Job
from g_challenge.src.core.db.create_schemas import ALLOWED_ENTITIES
router = APIRouter()

@router.post("/import-from-csv/{entity}/")
async def upload_job_csv(entity: str, file: UploadFile = File(...)):
    '''
    Allowed entities:
        jobs
        departments
        hiredEmployees
    '''
    if entity not in ALLOWED_ENTITIES.keys():
        return
    entity_obj = ALLOWED_ENTITIES[entity]
    response = await entity_obj.instert_from_csv(file)
    return {"response": response}
