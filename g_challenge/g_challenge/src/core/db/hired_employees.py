from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from g_challenge.src.core.db.db_connect import ENGINE, BASE

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