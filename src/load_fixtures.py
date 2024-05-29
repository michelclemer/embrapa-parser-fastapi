import json
from sqlmodel import SQLModel, Session, create_engine, select
from src.infra.settings import settings
from src.crud.models.embrapa import TypeExportModel, TypeProcessModel, TypeImportModel

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def load_json_data(path):
    with open(path, 'r') as file:
        return json.load(file)

def insert_data(session, model, data_list):
    for data in data_list:
        query = select(model).where(model.id == data['id'])
        if not session.exec(query).first():
            item = model(**data)
            session.add(item)
    session.commit()

def load_type_export():
    with Session(engine) as session:
        data = load_json_data('fixtures/TypeExport.json')
        insert_data(session, TypeExportModel, data)

def load_type_process():
    with Session(engine) as session:
        data = load_json_data('fixtures/TypeProcess.json')
        insert_data(session, TypeProcessModel, data)

def load_type_import():
    with Session(engine) as session:
        data = load_json_data('fixtures/TypeImport.json')
        insert_data(session, TypeImportModel, data)

if __name__ == '__main__':
    load_type_export()
    load_type_process()
    load_type_import()

