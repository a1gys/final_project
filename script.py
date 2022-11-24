from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

engine = create_engine("sqlite:///data/maindb.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

sql = "select codon, aminoacid_symbol from amino_acids"
df = pd.read_sql(sql, con=engine)

table = {codon: symbol for codon, symbol in 
    zip(df.codon.to_list(), df.aminoacid_symbol.to_list())}

def convert_dna_to_rna(sequence: str) -> str:
    new_sequence = sequence.replace('T', 'U')
    return new_sequence

def convert_rna_to_protein(sequence: str) -> str:
    protein = ''
    if len(sequence) % 3 == 1:
        sequence = sequence[:-1]
    elif len(sequence) % 3 == 2:
        sequence = sequence[:-2]
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        protein += table[codon]
    return protein

