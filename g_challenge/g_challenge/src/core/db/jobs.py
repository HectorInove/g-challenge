from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from g_challenge.src.core.db.db_connect import ENGINE, BASE


class Job(BASE):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    job = Column(String)
    hired_employees = relationship('Hired_employees', back_populates='job')

    @staticmethod
    def __delete_schema__():
        '''Delete table'''
        BASE.metadata.tables['jobs'].drop(ENGINE)

    @staticmethod
    def __create_all_schemas__():
        '''Create table'''
        BASE.metadata.create_all(ENGINE)