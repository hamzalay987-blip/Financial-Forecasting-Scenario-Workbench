import os
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from main import run

class ProjectTests(unittest.TestCase):
    def setUp(self):
        os.chdir(ROOT)

    def test_representative_sample(self):
        result=run()
        expected={'baseline': [1400.0, 1500.0, 1600.0], 'upside': [1430.0, 1560.0, 1690.0], 'downside': [1350.0, 1400.0, 1450.0], 'holdout_abs_error': 0.0}
        for key,value in expected.items():
            self.assertEqual(result[key],value, f'Mismatch on {key}')

    def test_replay_consistency(self):
        self.assertEqual(run(),run())

if __name__=='__main__':
    unittest.main()
