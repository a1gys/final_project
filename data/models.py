from sqlalchemy import Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DNA(Base):
    __tablename__ = "dna_bases"

    id_ = Column("id", Integer, primary_key=True)
    base = Column("base", CHAR)

    def __init__(self, id_, base):
        self.id_ = id_
        self.base = base
    
    def __repr__(self):
        return f"{self.base}"

class RNA(Base):
    __tablename__ = "rna_bases"

    id_ = Column("id", Integer, primary_key=True)
    base = Column("base", CHAR)

    def __init__(self, id_, base):
        self.id_ = id_
        self.base = base
    
    def __repr__(self):
        return f"{self.base}"

class Aminoacid(Base):
    __tablename__ = "amino_acids"

    id_ = Column("id", Integer, primary_key=True)
    codon = Column("codon", String)
    aminoacid_sign = Column("aminoacid_symbol", CHAR)

    def __init__(self, id_, codon, symbol):
        self.id_ = id_
        self.codon = codon
        self.aminoacid_sign = symbol
    
    def __repr__(self):
        return f"{self.codon} - {self.aminoacid_sign}"
