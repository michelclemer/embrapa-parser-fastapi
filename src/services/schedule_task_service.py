import datetime
import requests
import pandas as pd
from pandas.api.types import is_number
from io import StringIO
from sqlmodel import SQLModel, Session, create_engine, select
from src.infra.settings import settings
from src.crud.models.embrapa import ProductionModel, ImportModel, ExportModel, ProcessProductModel, ComercializationModel
class TaskServices:
    @staticmethod
    def example_task():
        print(f"Task executed at {datetime.datetime.now()}")


class ScrapingServices:
    @staticmethod
    def example_scraping():
        print(f"Scraping executed at {datetime.datetime.now()}")

    def make_scraping(self):
        requests.get("http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv")

    def handle_producao_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep=';')
            print("Produção")
            return df

    def handle_processamento_viniferas_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep='\t')
            print("Processamento Viniferas")
            return df

    def handle_processamento_americanas_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep='\t')
            print("Processamento Americanas")
            return df

    def handle_processamento_uva_mesa_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep='\t')
            this_year = datetime.datetime.now().year
            cols = [col for col in df.columns if col.isdigit() and 1970 <= int(col) <= this_year]
            print("Processamento Uva Mesa")
            return df


    def handle_sem_classificacao_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep='\t')
            print("Sem Classificação")
            return df

    def handle_comercializacao_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep=';')
            print("Comercialização")
            return df

    def handle_importacao_vinhos_mesa_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep=';')
            print("Importação Vinhos Mesa")
            return df

    def handle_importacao_vinhos_espumante_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep=';')
            print("Importação Vinhos Espumante")
            return df

    def handle_importacao_uva_fresca_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep=';')
            print("Importação Uva Fresca")
            return df

    def handle_importacao_uva_passas_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep=';')
            print("Importação Uva Passas")
            return df


    def handle_importacao_suco_uva_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep=';')
            print("Importação Suco Uva")
            return df

    def handle_exportacao_vinhos_mesa_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep=';')
            print("Exportação Vinhos Mesa")
            return df

    def handle_exportacao_vinhos_espumante_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep=';')
            print("Exportação Vinhos Espumante")
            return df

    def handle_exportacao_uva_fresca_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep=';')
            print("Exportação Uva Fresca")
            return df

    def handle_exportacao_suco_uva_data(self):
        resp = requests.get("http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv")
        if resp.status_code == 200:
            data = StringIO(resp.content.decode('utf-8'))
            df = pd.read_csv(data, sep=';')
            print("Exportação Suco Uva")
            return df


class HandelDB:
    def __init__(self):
        self.scraping = ScrapingServices()
        print(settings.SQLALCHEMY_DATABASE_URI)
        self.engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

    def __getet_years(self, df):
        this_year = datetime.datetime.now().year
        return [col for col in df.columns if col.isdigit() and 1970 <= int(col) <= this_year]

    def insert_producao(self):
        df = self.scraping.handle_producao_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_product": row["id"],
                    "control_label": row["control"],
                    "production_name": row["produto"],
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_liters"] = self.__quantity_kg(row, year)
                    query = select(ProductionModel).where(ProductionModel.id_product == new_row["id_product"], ProductionModel.year == new_row["year"], ProductionModel.control_label == new_row["control_label"])
                    if not session.exec(query).first():
                        item = ProductionModel(**new_row)
                        session.add(item)
            session.commit()

    def __quantity_kg(self, row, year) -> int:
        print(row[year], type(row[year]))
        if is_number(row[year]):
            return row[year]
        return 0

    def insert_processamento_viniferas(self):
        df = self.scraping.handle_processamento_viniferas_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_product": row["id"],
                    "control_label": row["control"],
                    "cultivar_name": row["cultivar"],
                    "type_process_id": 1
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_kg"] = self.__quantity_kg(row, year)
                    query = select(ProcessProductModel).where(ProcessProductModel.id_product == new_row["id_product"], ProcessProductModel.year == new_row["year"], ProcessProductModel.control_label == new_row["control_label"])
                    if not session.exec(query).first():
                        item = ProcessProductModel(**new_row)
                        session.add(item)
            session.commit()

    def insert_processamento_americanas(self):
        df = self.scraping.handle_processamento_americanas_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_product": row["id"],
                    "control_label": row["control"],
                    "cultivar_name": row["cultivar"],
                    "type_process_id": 2
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_kg"] = self.__quantity_kg(row, year)
                    query = select(ProcessProductModel).where(ProcessProductModel.id_product == new_row["id_product"], ProcessProductModel.year == new_row["year"], ProcessProductModel.control_label == new_row["control_label"])
                    if not session.exec(query).first():
                        item = ProcessProductModel(**new_row)
                        session.add(item)
            session.commit()

    def insert_processamento_uva_mesa(self):
        df = self.scraping.handle_processamento_uva_mesa_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_product": row["id"],
                    "control_label": row["control"],
                    "cultivar_name": row["cultivar"],
                    "type_process_id": 3
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_kg"] = self.__quantity_kg(row, year)
                    query = select(ProcessProductModel).where(
                        ProcessProductModel.id_product == new_row["id_product"], ProcessProductModel.year == new_row["year"], ProcessProductModel.control_label == new_row["control_label"])
                    if not session.exec(query).first():
                        item = ProcessProductModel(**new_row)
                        session.add(item)
            session.commit()

    def insert_processamento_sem_classificacao(self):
        df = self.scraping.handle_sem_classificacao_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_product": row["id"],
                    "control_label": row["control"],
                    "cultivar_name": row["cultivar"],
                    "type_process_id": 4
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_kg"] = self.__quantity_kg(row, year)
                    query = select(ProcessProductModel).where(ProcessProductModel.id_product == new_row["id_product"], ProcessProductModel.year == new_row["year"])
                    if not session.exec(query).first():
                        item = ProcessProductModel(**new_row)
                        session.add(item)
            session.commit()

    def insert_comercializacao(self):
        df = self.scraping.handle_comercializacao_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():

                default = {
                    "id_product": row["id"],
                    "control_label": row["control"],
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_liters"] = self.__quantity_kg(row, year)
                    try:
                        query = select(ComercializationModel).where(ComercializationModel.id_product == new_row["id_product"],
                                                                  ComercializationModel.year == new_row["year"], ComercializationModel.control_label == new_row["control_label"])
                        print(row)
                        if not session.exec(query).first():
                            item = ComercializationModel(**new_row)
                            session.add(item)
                    except:
                        pass
            session.commit()

    def insert_importacao_vinhos_mesa(self):
        df = self.scraping.handle_importacao_vinhos_mesa_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_product": row["Id"],
                    "country_origin": row["País"],
                    "type_import_id": 1
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_kg"] = self.__quantity_kg(row, year)
                    new_row["price_uss"] = f'{row[year]}.1'
                    query = select(ImportModel).where(ImportModel.id_product == new_row["id_product"],
                                                              ImportModel.year == new_row["year"], ImportModel.type_import_id == new_row["type_import_id"])
                    if not session.exec(query).first():
                        item = ImportModel(**new_row)
                        session.add(item)
            session.commit()

    def insert_importacao_vinhos_espumante(self):
        df = self.scraping.handle_importacao_vinhos_espumante_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_product": row["Id"],
                    "country_origin": row["País"],
                    "type_import_id": 2
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_kg"] = self.__quantity_kg(row, year)
                    new_row["price_uss"] = f'{row[year]}.1'
                    query = select(ImportModel).where(ImportModel.id_product == new_row["id_product"],
                                                              ImportModel.year == new_row["year"], ImportModel.type_import_id == new_row["type_import_id"])
                    if not session.exec(query).first():
                        item = ImportModel(**new_row)
                        session.add(item)
            session.commit()

    def insert_importacao_uva_fresca(self):
        df = self.scraping.handle_importacao_uva_fresca_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_product": row["Id"],
                    "country_origin": row["País"],
                    "type_import_id": 3
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_kg"] = self.__quantity_kg(row, year)
                    new_row["price_uss"] = f'{row[year]}.1'
                    query = select(ImportModel).where(ImportModel.id_product == new_row["id_product"],
                                                              ImportModel.year == new_row["year"], ImportModel.country_origin == new_row["country_origin"])
                    if not session.exec(query).first():
                        item = ImportModel(**new_row)
                        session.add(item)
            session.commit()

    def insert_importacao_uva_passas(self):
        df = self.scraping.handle_importacao_uva_passas_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_product": row["Id"],
                    "country_origin": row["País"],
                    "type_import_id": 4
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_kg"] = self.__quantity_kg(row, year)
                    new_row["price_uss"] = f'{row[year]}.1'
                    query = select(ImportModel).where(ImportModel.id_product == new_row["id_product"],
                                                              ImportModel.year == new_row["year"], ImportModel.country_origin == new_row["country_origin"])
                    if not session.exec(query).first():
                        item = ImportModel(**new_row)
                        session.add(item)
            session.commit()

    def insert_importacao_suco_uva(self):
        df = self.scraping.handle_importacao_suco_uva_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_product": row["Id"],
                    "country_origin": row["País"],
                    "type_import_id": 5
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_kg"] = self.__quantity_kg(row, year)
                    new_row["price_uss"] = f'{row[year]}.1'
                    query = select(ImportModel).where(ImportModel.id_product == new_row["id_product"],
                                                              ImportModel.year == new_row["year"], ImportModel.country_origin == new_row["country_origin"])
                    if not session.exec(query).first():
                        item = ImportModel(**new_row)
                        session.add(item)
            session.commit()

    def insert_exportacao_vinhos_mesa(self):
        df = self.scraping.handle_exportacao_vinhos_mesa_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_product": row["Id"],
                    "country_origin": row["País"],
                    "type_export_id": 1
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_kg"] = self.__quantity_kg(row, year)
                    new_row["price_uss"] = f'{row[year]}.1'
                    query = select(ExportModel).where(ExportModel.id_product == new_row["id_product"],
                                                              ExportModel.year == new_row["year"], ExportModel.type_export_id == new_row["type_export_id"])
                    if not session.exec(query).first():
                        item = ExportModel(**new_row)
                        session.add(item)
            session.commit()

    def insert_exportacao_vinhos_espumante(self):
        df = self.scraping.handle_exportacao_vinhos_espumante_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_product": row["Id"],
                    "country_origin": row["País"],
                    "type_export_id": 2
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_kg"] = self.__quantity_kg(row, year)
                    new_row["price_uss"] = f'{row[year]}.1'
                    query = select(ExportModel).where(ExportModel.id_product == new_row["id_product"],
                                                              ExportModel.year == new_row["year"], ExportModel.type_export_id == new_row["type_export_id"])
                    if not session.exec(query).first():
                        item = ExportModel(**new_row)
                        session.add(item)
            session.commit()

    def insert_exportacao_uva_fresca(self):
        df = self.scraping.handle_exportacao_uva_fresca_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_product": row["Id"],
                    "country_origin": row["País"],
                    "type_export_id": 3
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_kg"] = self.__quantity_kg(row, year)
                    new_row["price_uss"] = f'{row[year]}.1'
                    if str(new_row['price_uss']).startswith('0.0.'):
                        new_row['price_uss'] = f'0.0{str(new_row["price_uss"])[2:]}'
                    try:
                        query = select(ExportModel).where(ExportModel.id_product == new_row["id_product"],
                                                          ExportModel.year == new_row["year"],
                                                          ExportModel.type_export_id == new_row["type_export_id"])
                        if not session.exec(query).first():
                            item = ExportModel(**new_row)
                            session.add(item)
                    except:
                        pass
            try:
                session.commit()
            except:
                pass

    def insert_exportacao_suco_uva(self):
        df = self.scraping.handle_exportacao_suco_uva_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_product": row["Id"],
                    "country_origin": row["País"],
                    "type_export_id": 4
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_kg"] = self.__quantity_kg(row, year)
                    new_row["price_uss"] = f'{row[year]}.1'
                    try:
                        query = select(ExportModel).where(ExportModel.id_product == new_row["id_product"],
                                                          ExportModel.year == new_row["year"],
                                                          ExportModel.type_export_id == new_row["type_export_id"])
                        if not session.exec(query).first():
                            item = ExportModel(**new_row)
                            session.add(item)
                    except:
                        pass
            session.commit()


    def insert_all(self):
        self.insert_producao()
        self.insert_processamento_viniferas()
        self.insert_processamento_americanas()
        self.insert_processamento_uva_mesa()
        self.insert_processamento_sem_classificacao()
        self.insert_comercializacao()
        self.insert_importacao_vinhos_mesa()
        self.insert_importacao_vinhos_espumante()
        self.insert_importacao_uva_fresca()
        self.insert_importacao_uva_passas()
        self.insert_importacao_suco_uva()
        self.insert_exportacao_vinhos_mesa()
        self.insert_exportacao_vinhos_espumante()
        self.insert_exportacao_uva_fresca()
        self.insert_exportacao_suco_uva()
        print("All data inserted")


insert_data = HandelDB()
