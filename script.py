from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from data.config import postgresql as setting

url = f"postgresql://{setting['pguser']}:{setting['pgpassword']}@{setting['pghost']}:{setting['pgport']}/{setting['pgdb']}"
engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

sql = "select codon, aminoacid_symbol from amino_acids"
df = pd.read_sql(sql, con=engine)

table = {codon: symbol for codon, symbol in 
    zip(df.codon.to_list(), df.aminoacid_symbol.to_list())}

def convert_dna_to_rna(sequence: str, complement: bool = False) -> str:
    """Function to convert dna sequence into rna sequence
    Parameters: sequence - string of bases to convert
                complement - boolean flag to indicate whether to complementary convert (default set to False)
                Complementary convert: A->U, T->A, C->G, G->C
    Returns: if complement set to True, complementary rna sequence will be returned
             if complement not set, rna sequence will be returned (T->U)
    """
    new_sequence = sequence.replace('T', 'U')

    if complement:
        complementary_seq = ""
        for base in new_sequence:
            if base == "U":
                complementary_seq += "A"
            elif base == "A":
                complementary_seq += "U"
            elif base == "G":
                complementary_seq += "C"
            elif base == "C":
                complementary_seq += "G"
        return complementary_seq

    return new_sequence

def convert_rna_to_protein(sequence: str) -> str:
    """Function to convert rna sequence into protein using 3-length bases (codons/triplets)
    Parameters: sequence - string of rna bases to convert
    Returns: protein sequence
    """
    protein = ''
    if len(sequence) % 3 == 1:
        sequence = sequence[:-1]
    elif len(sequence) % 3 == 2:
        sequence = sequence[:-2]
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        protein += table[codon]
    return protein