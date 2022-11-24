import unittest
import script

class ConverterTest(unittest.TestCase):
    
    def test_long_sequences(self):
        self.assertEqual(script.convert_dna_to_rna('ATTTGGCTACTAACAATCTA'), 'AUUUGGCUACUAACAAUCUA')
        self.assertEqual(script.convert_dna_to_rna('GTTGTAATGGCCTACATTA'), 'GUUGUAAUGGCCUACAUUA')
        self.assertEqual(script.convert_dna_to_rna('CAGGTGGTGTTGTTCAGTT'), 'CAGGUGGUGUUGUUCAGUU')
        self.assertEqual(script.convert_dna_to_rna('GCTAACTAAC'), 'GCUAACUAAC')
        self.assertEqual(script.convert_dna_to_rna('GCTAACTAACATCTTTGGCACTGTT'), 'GCUAACUAACAUCUUUGGCACUGUU')
        self.assertEqual(script.convert_dna_to_rna('TATGAAAAACTCAAA'), 'UAUGAAAAACUCAAA')
        self.assertEqual(script.convert_dna_to_rna('CCCGTCCTTGATTGGCTTGAAGAGAAGTTT'), 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU')

    def test_empty_sequence(self):
        self.assertEqual(script.convert_dna_to_rna(''), '')

if __name__ == '__main__':
    unittest.main()