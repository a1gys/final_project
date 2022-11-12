import unittest
import script

class ConverterTest(unittest.TestCase):
    
    def test_convert_dna_to_rna(self):
        self.assertEqual(script.convert_dna_to_rna('ATTTGGCTACTAACAATCTA'), 'AUUUGGCUACUAACAAUCUA')
        self.assertEqual(script.convert_dna_to_rna('GTTGTAATGGCCTACATTA'), 'GUUGUAAUGGCCUACAUUA')
        self.assertEqual(script.convert_dna_to_rna('CAGGTGGTGTTGTTCAGTT'), 'CAGGUGGUGUUGUUCAGUU')
        self.assertEqual(script.convert_dna_to_rna('GCTAACTAAC'), 'GCUAACUAAC')
        self.assertEqual(script.convert_dna_to_rna('GCTAACTAACATCTTTGGCACTGTT'), 'GCUAACUAACAUCUUUGGCACUGUU')
        self.assertEqual(script.convert_dna_to_rna('TATGAAAAACTCAAA'), 'UAUGAAAAACUCAAA')
        self.assertEqual(script.convert_dna_to_rna('CCCGTCCTTGATTGGCTTGAAGAGAAGTTT'), 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU')

    def test_convert_rna_to_protein(self):
        self.assertEqual(script.convert_rna_to_protein('AUUUGGCUACUAACAAUCUA'), 'IWLLTI')
        self.assertEqual(script.convert_rna_to_protein('GUUGUAAUGGCCUACAUUA'), 'VVMAYI')
        self.assertEqual(script.convert_rna_to_protein('CAGGUGGUGUUGUUCAGUU'), 'QVVLFS')
        self.assertEqual(script.convert_rna_to_protein('GCUAACUAAC'), 'AN.')
        self.assertEqual(script.convert_rna_to_protein('GCUAACUAACAUCUUUGGCACUGUU'), 'AN.HLWHC')
        self.assertEqual(script.convert_rna_to_protein('UAUGAAAAACUCAAA'), 'YEKLK')
        self.assertEqual(script.convert_rna_to_protein('CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'), 'PVLDWLEEKF')

if __name__ == '__main__':
    unittest.main()