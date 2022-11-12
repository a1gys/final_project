from data import data

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
        if data.SEQUENCES[codon] == 'Stop':
            protein += '.'
        else:
            protein += data.SEQUENCES[codon][0]

    return protein

