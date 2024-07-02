import unittest
from lamrand.lamrand import LamRand, LamRandSecure

class TestLamRand(unittest.TestCase):
    def setUp(self):
        self.randomizer = LamRand()

    def test_next_int(self):
        value = self.randomizer.next_int(1, 10)
        self.assertTrue(1 <= value <= 10)

    def test_next_float(self):
        value = self.randomizer.next_float()
        self.assertTrue(0 <= value < 1)

    def test_next_bool(self):
        value = self.randomizer.next_bool()
        self.assertIn(value, [True, False])

    def test_next_string(self):
        value = self.randomizer.next_string(10)
        self.assertEqual(len(value), 10)
        self.assertTrue(all(c.isalnum() for c in value))

    def test_shuffle(self):
        data = [1, 2, 3, 4, 5]
        shuffled = self.randomizer.shuffle(data[:])
        self.assertNotEqual(data, shuffled)
        self.assertCountEqual(data, shuffled)

    def test_next_gaussian(self):
        value = self.randomizer.next_gaussian()
        self.assertIsInstance(value, float)

    def test_next_gaussian_box_muller(self):
        value = self.randomizer.next_gaussian_box_muller()
        self.assertIsInstance(value, float)

    def test_next_poisson(self):
        value = self.randomizer.next_poisson(3.5)
        self.assertIsInstance(value, int)

    def test_save_load_state(self):
        state = self.randomizer.save_state()
        value1 = self.randomizer.next()
        self.randomizer.load_state(state)
        value2 = self.randomizer.next()
        self.assertEqual(value1, value2)

class TestLamRandSecure(unittest.TestCase):
    def setUp(self):
        self.randomizer = LamRandSecure()

    def test_next_int(self):
        value = self.randomizer.next_int(1, 10)
        self.assertTrue(1 <= value <= 10)

    def test_next_float(self):
        value = self.randomizer.next_float()
        self.assertTrue(0 <= value < 1)

    def test_next_bool(self):
        value = self.randomizer.next_bool()
        self.assertIn(value, [True, False])

    def test_next_string(self):
        value = self.randomizer.next_string(10)
        self.assertEqual(len(value), 10)
        self.assertTrue
        self.assertTrue(all(c.isalnum() for c in value))

if __name__ == '__main__':
    unittest.main()