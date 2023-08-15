from fastapi import FastAPI, File, UploadFile
from g_challenge.src.core.v1_schemas import (InsertJob, InsertDepartment, InsertHiredEmployees)
from fastapi import APIRouter
from g_challenge.src.core.db.jobs import Job
from g_challenge.src.core.db.departments import Department
from g_challenge.src.core.db.hired_employees import HiredEmployees
from g_challenge.src.core.db.create_schemas import ALLOWED_ENTITIES
router = APIRouter()

@router.post("/import-from-csv/{entity}/", tags=["Import API"])
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


@router.post("/insert/job/", tags=["Job APIs"])
async def insert_job(body_params : InsertJob):
    '''
    '''
    result = await Job.insert_jobs(body_params.jobs)
    return result


@router.post("/insert/department/", tags=["Department APIs"])
async def insert_department(body_params : InsertDepartment):
    '''
    '''
    result = await Department.insert_departments(body_params.departments)
    return result

@router.post("/insert/hired-employees/", tags=["Hired employees APIs"])
async def insert_hired_employee(body_params : InsertHiredEmployees):
    '''
    '''
    result = await HiredEmployees.insert_hired_employees(body_params.hired_employees)
    return result


@router.get("/hired-employees-by-quarter/", tags=["Hired employees APIs"])
async def get_hired_employees_by_quarter(year: int = 2021):
    '''
    '''
    result = await HiredEmployees.get_by_quarter(year)
    return result

@router.get("/get-departments-above-average/", tags=["Hired employees APIs"])
async def departments_above_average(year: int = 2021):
    '''
    '''
    result = await HiredEmployees.get_departments_above_average(year)
    return result