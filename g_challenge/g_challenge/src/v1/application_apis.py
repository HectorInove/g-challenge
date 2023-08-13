from fastapi import FastAPI, File, UploadFile

from fastapi import APIRouter
from g_challenge.src.core.db.jobs import Job
router = APIRouter()


@router.post("/")
def update_admin():
    return {"message": "Admin getting schwifty"}


@router.post("/files/")
def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@router.post("/uploadfile/")
async def upload_job_csv(file: UploadFile = File(...)):
    import csv
    # f_content = await file.read()
    # if file.filename.lower().endswith('.csv'):
    #     csvreaded = csv.reader(f_content.decode('utf-8').replace('\r\n', '\n').split('\n'))
    #     next(csvreaded)
    #     for row in csvreaded:
    #         print(row)
    response = await Job.instert_from_csv(file)
    return {"response": response}
