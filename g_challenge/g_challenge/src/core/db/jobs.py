from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from g_challenge.src.core.db.db_connect import ENGINE, BASE, SESSION
import csv
from sqlalchemy import insert


class Job(BASE):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    job = Column(String)
    # hired_employees = relationship('Hired_employees', back_populates='job')

    @staticmethod
    def __delete_schema__():
        '''Delete table'''
        BASE.metadata.tables['jobs'].drop(ENGINE)

    @staticmethod
    def __create_all_schemas__():
        '''Create table'''
        BASE.metadata.create_all(ENGINE)

    @staticmethod
    async def instert_from_csv(file):
        result = {'valids':[], 'invalids':[]}
        import csv

        f_content = await file.read()
        if file.filename.lower().endswith('.csv'):
            csvreaded = csv.reader(f_content.decode('utf-8').replace('\r\n', '\n').split('\n'))
            next(csvreaded)
            to_insert = []
            for element in csvreaded:
                try:
                    to_insert.append({
                        'id':int(element[0]),
                        'job':str(element[1])
                        }
                    )
                except:
                    result['invalids'].append(
                        {'id':element[0], 'job':element[1]}
                    )
                print(element)
            session = SESSION()
            returns = session.execute(
                insert(Job).returning(Job),
                to_insert
                )
        result['valids'] = returns
        return result