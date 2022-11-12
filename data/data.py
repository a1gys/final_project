'''
TABLE dna_bases
|id|base|

TABLE rna_bases
|id|base| -> id foreign key to dna_bases.id

TABLE amino_acids
|id|base(triplets)|corresponding aminoacid|
'''





SEQUENCES = {
    'UUU': 'F(Phe)', 'UUC': 'F(Phe)',
    'UUA': 'Leu', 'UUG': 'Leu', 'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser', 'AGU': 'Ser', 'AGC': 'Ser',
    'UAU': 'Y(Tyr)', 'UAC': 'Y(Tyr)',
    'UAA': '.', 'UAG': '.', 'UGA': '.',
    'UGU': 'Cys', 'UGC': 'Cys',
    'UGG': 'W(Trp)',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'CAU': 'His', 'CAC': 'His',
    'CAA': 'Q(Gln)', 'CAG': 'Q(Gln)', 
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AGA': 'Arg', 'AGG': 'Arg',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
    'AUG': 'Met',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'AAU': 'N(Asn)', 'AAC': 'N(Asn)',
    'AAA': 'K(Lys)', 'AAG': 'K(Lys)',
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'GAU': 'D(Asp)', 'GAC': 'D(Asp)',
    'GAA': 'E(Glu)', 'GAG': 'E(Glu)',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}