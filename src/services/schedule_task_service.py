import datetime
import requests
import pandas as pd
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
                    new_row["quantity_liters"] = row[year]
                    query = select(ProductionModel).where(ProductionModel.id_product == new_row["id_product"], ProductionModel.year == new_row["year"])
                    if not session.exec(query).first():
                        item = ProductionModel(**new_row)
                        session.add(item)
            session.commit()

    def __quantity_kg(self, row, year) -> int:
        print(row[year], type(row[year]))
        if not pd.isna(row[year]):
            return row[year]
        return 0

    def insert_processamento_viniferas(self):
        df = self.scraping.handle_processamento_viniferas_data()
        years = self.__getet_years(df)
        with Session(self.engine) as session:
            for index, row in df.iterrows():
                default = {
                    "id_process": row["id"],
                    "control_label": row["control"],
                    "cultivar_name": row["cultivar"],
                    "type_process_id": 1
                }
                for year in years:
                    new_row = default.copy()
                    new_row["year"] = year
                    new_row["quantity_kg"] = self.__quantity_kg(row, year)
                    query = select(ProcessProductModel).where(ProcessProductModel.id_process == new_row["id_process"], ProcessProductModel.year == new_row["year"])
                    if not session.exec(query).first():
                        item = ProcessProductModel(**new_row)
                        session.add(item)
            session.commit()

    def insert_processamento_americanas(self):
        pass

    def insert_processamento_uva_mesa(self):
        pass

    def insert_sem_classificacao(self):
        pass

    def insert_comercializacao(self):
        pass

    def insert_importacao_vinhos_mesa(self):
        pass

    def insert_importacao_vinhos_espumante(self):
        pass

    def insert_importacao_uva_fresca(self):
        pass

    def insert_importacao_uva_passas(self):
        pass

    def insert_importacao_suco_uva(self):
        pass

    def insert_exportacao_vinhos_mesa(self):
        pass

    def insert_exportacao_vinhos_espumante(self):
        pass

    def insert_exportacao_uva_fresca(self):
        pass

    def insert_exportacao_suco_uva(self):
        pass


teste = HandelDB()
teste.insert_processamento_viniferas()
