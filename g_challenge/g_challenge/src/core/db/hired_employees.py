import csv
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from g_challenge.src.core.db.db_connect import ENGINE, BASE, excecute
from sqlalchemy import insert

class HiredEmployees(BASE):
    __tablename__ = 'hired_employees'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    datetime = Column(DateTime)
    department_id = Column(Integer, ForeignKey('departments.id'))
    job_id = Column(Integer, ForeignKey('jobs.id'))

    @staticmethod
    def __delete_schema__():
        '''Delete table'''
        BASE.metadata.tables['hired_employees'].drop(ENGINE)

    @staticmethod
    def __create_all_schemas__():
        '''Create table'''
        BASE.metadata.create_all(ENGINE)


    @staticmethod
    async def instert_from_csv(file):
        result = {'valids':[], 'invalids':[]}
        f_content = await file.read()
        if file.filename.lower().endswith('.csv'):
            to_insert = []
            csvreaded = csv.reader(f_content.decode('utf-8').replace('\r\n', '\n').split('\n'))
            for element in csvreaded:
                if element != []:
                    try:
                        stmt = insert(HiredEmployees).values(
                            id= int(element[0]),
                            name= str(element[1]),
                            datetime= str(element[2]) if element[2] != '' else None,
                            department_id= int(element[3]) if element[3].isdigit() else None,
                            job_id= int(element[4]) if element[4].isdigit() else None
                            ).returning(HiredEmployees)
                        query_result = excecute(stmt).fetchone()
                        to_insert.append({
                            'id': int(query_result[0]),
                            'name': str(query_result[1]),
                            'datetime': str(query_result[2]),
                            'department_id': int(query_result[3]) if isinstance(query_result[3], int) else None,
                            'job_id': int(query_result[4]) if isinstance(query_result[4], int) else None
                            }
                        )
                    except Exception as e:
                            result['invalids'].append({
                            'id': element[0],
                            'name': element[1],
                            'datetime': element[2],
                            'department_id': element[3],
                            'job_id': element[4]
                            }
                        )
                    print(element)
        result['valids'] = to_insert
        return result