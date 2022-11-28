from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from data import SEQUENCES as seq
from config import postgresql as setting
from models import Base, DNA, RNA, Aminoacid

def get_engine(user: str, password: str, host: str, port: int, db: str):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine 

engine = get_engine(setting['pguser'], setting['pgpassword'], setting['pghost'], setting['pgport'], setting['pgdb'])


#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

bases = [DNA(1, "A"), DNA(2, "T"), DNA(3, "C"), DNA(4, "G")]
for base in bases:
    session.add(base)
session.commit()

bases = [RNA(1, "A"), RNA(2, "U"), RNA(3, "C"), RNA(4, "G")]
for base in bases:
    session.add(base)
session.commit()

aminoacids = []

for (k, v), id_ in zip(seq.items(), range(1, len(seq) + 1)):
    aminoacids.append(Aminoacid(id_, k, v[0]))
for aminoacid in aminoacids:
    session.add(aminoacid)
session.commit()

session.close()