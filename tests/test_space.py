import numpy as np
import unittest
from numpy_space.space import Space

class TestSpaceMethods(unittest.TestCase):
    
    def test_print(self):
        x = [np.array([1,2,3]), np.array([2,3,4])]
        V = Space(x)
        self.assertEqual(V.__str__(), "{[1 2 3], [2 3 4]}")

        y = [np.array([1,2,3]), np.array([1,2,3]), np.array([2,3,4])]
        U = Space(y)
        self.assertEqual(U.__str__(), "{[1 2 3], [2 3 4]}")


    def test_add(self):
        x = [np.array([1,2,3])]
        y = [np.array([2,3,4])]
        z = [np.array([1,2,3]), np.array([2,3,4])]
        V = Space(x)
        U = Space(y)
        W = Space(z)
        # print(V+U)
        # print(W)
        self.assertSetEqual((V+U).space, W.space)

    def test_mul(self):
        x = [np.array([1,2,3]), np.array([2,3,4])]
        y = [np.array([2,3,4]), np.array([4,5,6])]
        z = [np.array([2,3,4])]
        V = Space(x)
        U = Space(y)
        W = Space(z)
        # print(V*U)
        # print(W)
        self.assertSetEqual((V*U).space, W.space)

if __name__ == "__main__":
    unittest.main()
