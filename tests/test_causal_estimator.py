import unittest
import os
import pandas as pd
import numpy as np
from tests.definitions import DATA_PATH

class TestCausalEstimator(unittest.TestCase):
    def setUp(self):
        #self.df = pd.read_csv(os.path.join(DATA_PATH,'dgp_1/acic_1_1_data.csv'))
        #self.ate = np.mean(self.df['y1'] - self.df['y0'])
        #treated = self.df[self.df['z']==1]
        #self.att = np.mean(treated['y1'] - treated['y0'])
        self.df=None
        self.ate=1

    #def test_average_treatment_effect(self):
    #     est_ate = 1
    #     bias = est_ate - self.ate
    #     print(bias)
    #     self.assertAlmostEqual(self.ate, est_ate)

    #def test_average_treatment_effect_on_treated(self):
    #    est_att = 1
    #    self.att=1
    #    bias = est_att - self.att
    #    print(bias)
    #    self.assertAlmostEqual(self.att, est_att)


if __name__=="__main__":
    unittest.main()
