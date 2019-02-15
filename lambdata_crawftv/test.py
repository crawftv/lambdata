from top_x import top_x
import pandas as pd
import unittest

df = pd.DataFrame([1,1,1,1,2,2,3,3,3,4,5,5,5,5,5], columns=['n'])


class Test(unittest.TestCase):

    def test_propper(self):
        self.assertTrue(type(top_x(df,'n',3))==pd.DataFrame)
      
    def test_improper(self):
        with self.assertRaises(TypeError):
            top_x()
        with self.assertRaises(TypeError):
            top_x(df)
        with self.assertRaises(TypeError):
            top_x(df,'n')
          


if __name__ == '__main__':
    unittest.main()
