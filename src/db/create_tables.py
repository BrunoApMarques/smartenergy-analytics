from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData
from src.db.connection import get_engine

def create_tables():
    engine = get_engine()
    metadata = MetaData()

    interrupcoes = Table(
        'interrupcoes',
        metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('id_ocorrencia', Integer, nullable=False),
        Column('data_abertura', DateTime, nullable=False),
        Column('data_fechamento', DateTime),
        Column('regiao', String(100)),
        Column('causa', String(100)),
        Column('clientes_afetados', Integer),
        Column('status', String(50)),
        Column('duracao_min', Integer)
    )

    metadata.create_all(engine)
    print("Tabela criada com sucesso!")

if __name__ == "__main__":
    create_tables()
