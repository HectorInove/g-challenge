from g_challenge.src.core.db.jobs import Job
from g_challenge.src.core.db.departments import Department
from g_challenge.src.core.db.hired_employees import HiredEmployees

ALLOWED_ENTITIES = {
        'jobs':Job,
        'departments':Department,
        'hiredEmployees': HiredEmployees
        }

def create_all_schemas():
    Job.__create_all_schemas__()
    HiredEmployees.__create_all_schemas__()
    Department.__create_all_schemas__()