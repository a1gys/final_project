import sqlalchemy
from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

'''with engine.connect() as conn:
    conn.execute(text("CREATE TABLE dna_bases (id int, base str)"))
    conn.execute(text("INSERT INTO dna_bases (id, base) VALUES (:id, :base)"), 
            [{"id": 1, "base": "A"}, {"id": 2, "base": "C"}, {"id": 3, "base": "T"}, {"id": 4, "base": "G"}])
    conn.commit()'''

with engine.begin() as conn:
    conn.execute(text("CREATE TABLE dna_bases (id int, base str)"))
    conn.execute(text("INSERT INTO dna_bases (id, base) VALUES (:id, :base)"), 
            [{"id": 1, "base": "A"}, {"id": 2, "base": "C"}, {"id": 3, "base": "T"}, {"id": 4, "base": "G"}])
