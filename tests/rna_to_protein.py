import unittest
import script

class ConverteToProteinTest(unittest.TestCase):

    def test_long_sequences(self):
        self.assertEqual(script.convert_rna_to_protein('AUUUGGCUACUAACAAUCUA'), 'IWLLTI')
        self.assertEqual(script.convert_rna_to_protein('GUUGUAAUGGCCUACAUUA'), 'VVMAYI')
        self.assertEqual(script.convert_rna_to_protein('CAGGUGGUGUUGUUCAGUU'), 'QVVLFS')
        self.assertEqual(script.convert_rna_to_protein('UAUGAAAAACUCAAA'), 'YEKLK')
        self.assertEqual(script.convert_rna_to_protein('CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'), 'PVLDWLEEKF')

    def test_with_stop_codon(self):
        self.assertEqual(script.convert_rna_to_protein('GCUAACUAAC'), 'AN.')
        self.assertEqual(script.convert_rna_to_protein('GCUAACUAACAUCUUUGGCACUGUU'), 'AN.HLWHC')

    def test_empty_sequence(self):
        self.assertEqual(script.convert_rna_to_protein(''), '')

if __name__ == "__main__":
    unittest.main()