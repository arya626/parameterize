import unittest
from parameterize.calculate import volume


class TestVolume(unittest.TestCase):

    def test_volume_positive_radius(self):
        self.assertAlmostEqual(volume(1), 4.1887902047863905)
        self.assertAlmostEqual(volume(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            volume(-1)


if __name__ == '__main__':
    unittest.main()
